import RPi.GPIO as GPIO
import time
import socket
from threading import Thread

# For receving data from the node
HOST = '0.0.0.0'
PORT = 10000
context = -1


relayPin1 = 19
relayPin2 = 13	
pirPin1 = 26
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(relayPin1, GPIO.OUT)
GPIO.setup(relayPin2, GPIO.OUT)
GPIO.setup(pirPin1, GPIO.IN)

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

last = 0
while True:
        time.sleep(0.5)
        cur = time.time()
        print "hub ", context
	if context == 1:
		GPIO.output(19, GPIO.HIGH)
                time.sleep(0.5)
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
