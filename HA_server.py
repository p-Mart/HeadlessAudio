import pyaudio
import socket
import base64

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100

#Socket instance
s = socket.socket()
host = '192.168.1.65'
port = 8080
s.bind((host, port))

s.listen(1) #Only allow one connection for right now

#Pyaudio instance
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE,
                input=True,
				input_device_index = 2,
                output=False,
                frames_per_buffer=CHUNK)

client, address = s.accept()
print "Got connection from ", address
	
while True:
	
	data = stream.read(CHUNK)
	encoded_data = base64.b64encode(data)
	client.send(encoded_data)
	
stream.close()
p.terminate()	



