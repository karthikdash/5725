import RPi.GPIO as GPIO
import time
import socket


# For sending data from node to hub via sockets
HOST = '127.0.0.1'
PORT = 10000

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.connect((HOST, PORT))

pirPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)

data = {}
data["node0"] = "1"


while True:
	if GPIO.input(pirPin):
		data["node0"] = "1"
		sendSocket.sendall(data["node0"].encode())
		#
		#
		# Enter the communication code such that the Node sends a signal to the Hub
		#
		#
	else:
		data["node0"] = "0"
		sendSocket.sendall(data["node0"].encode())
		#
		#
		# Logic when Node does not detect anything.
		#
		#

