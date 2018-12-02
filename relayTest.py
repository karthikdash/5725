import RPi.GPIO as GPIO
import time
import socket


# For sending data from node to hub via sockets
HOST = '192.168.43.74'
PORT = 10000

pirPin = 26
relayPin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(relayPin, GPIO.OUT)

data = {}
data["node0"] = "1"

# Triggering the relay
last_movement_time = 0
last_relay_time = 0
time_relay_on = 10

while True:
    time.sleep(0.1)
    if GPIO.input(pirPin):
        print 1
        last_movement_time = time.time()
        # GPIO.output(relayPin, GPIO.HIGH)
        # sendSocket.sendall(data["node0"].encode())
    else:
        print 0
        data["node0"] = "0"
        # GPIO.output(relayPin, GPIO.LOW)
        # sendSocket.sendall(data["node0"].encode())
    if time.time() - last_movement_time > time_relay_on:
        GPIO.output(relayPin, GPIO.LOW)
        print "Relay OFF"
    else:
        if last_movement_time != 0:
            GPIO.output(relayPin, GPIO.HIGH)
            print "Relay ON"
