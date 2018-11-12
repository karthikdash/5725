import RPi.GPIO as GPIO
import time
import socket
from threading import Thread

# For receving data from the node
HOST = '127.0.0.1'
PORT = 10000
context = -1


relayPin1 = 19
relayPin2 = 13	

GPIO.setmode(GPIO.BCM)

GPIO.setup(relayPin1, GPIO.OUT)
GPIO.setup(relayPin2, GPIO.OUT)

class ListenThread(Thread):
    def __init__(self):
        Thread.__init__(self)


    def run(self):
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.bind((HOST, PORT))
        self.recvSocket.listen(0)
        conn, addr = self.recvSocket.accept()
        print(conn,addr)
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
                print("Here")
            try:
                global context
                context = int(data)
            except Exception as e:
                print e

thread = ListenThread()
thread.start()


while True:
	if context == 1:
		GPIO.output(19, GPIO.HIGH)
	else:
		GPIO.output(19, GPIO.LOW)
	#
	#
	# Write logic such that this hub receives some signal from the hub and Triggers the Relay ON
	#
	#

	#
	#
	# Write logic such that this hub receives some signal from the hub and Triggers the Relay OFF
	#
	#