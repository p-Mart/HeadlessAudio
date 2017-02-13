import pyaudio
import socket
import base64

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

#Socket instance
s = socket.socket()
host = '192.168.1.65'
port = 8080

s.connect((host, port))

#Pyaudio instance
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=False,
                output=True,
				output_device_index = 2,
                frames_per_buffer=CHUNK)

print s.recv(1024)
				
while True:
	encoded_data = s.recv(1024) #It probably doesn't have to be this big of a buffer but I'll optimize it later
	decoded_data = base64.b64decode(encoded_data)
	stream.write(decoded_data)

	
stream.close()
p.terminate()	



