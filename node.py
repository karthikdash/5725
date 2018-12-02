import RPi.GPIO as GPIO
import time
import socket
import json

# For sending data from node to hub via sockets
HOST = '192.168.43.74'
PORT = 10000

sendSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendSocket.connect((HOST, PORT))

pirPin  = 26
pirPin1 = 13

relayPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(pirPin1, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)

data = {}
data["node"] = "-1"
data["node1"] = "-1"
data["id"] = "0"
data["posX"] = "250"
data["posY"] = "25"
data["pos1X"] = "50"
data["pos1Y"] = "25"

# Triggering the relay
last_movement_time = 0
last_relay_time = 0
time_relay_on = 10

# Triggering the relay
last_movement_time1 = 0
last_relay_time1 = 0
time_relay_on1 = 10

while True:

    time.sleep(0.1)
    if GPIO.input(pirPin):
        print 1,
        last_movement_time = time.time()
    else:
        print 0,


    if time.time() - last_movement_time > time_relay_on:
        GPIO.output(relayPin, GPIO.LOW)
        print " Relay0 OFF"
        data["node"] = "0"

    else:
        if last_movement_time != 0:
            GPIO.output(relayPin, GPIO.HIGH)
            print " Relay0 ON"
            data["node"] = "1"

    
    if GPIO.input(pirPin1):
        print 1,
        last_movement_time1 = time.time()
    else:
        print 0,

    if time.time() - last_movement_time1 > time_relay_on1:
        print " Relay1 OFF"
        data["node1"] = "0"

    else:
        if last_movement_time1 != 0:
            print " Relay1 ON"
            data["node1"] = "1"
    


    sendSocket.sendall(json.dumps(data).encode())
