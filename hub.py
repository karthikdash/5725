import RPi.GPIO as GPIO
import time
import socket
from threading import Thread
import pygame
import os
import time

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()

size = width, height = 320, 240
speed = [2,2]
speed1 = [2,2]
black = 20,20,40
white = 255,255,255
blue = 0,0,255
red = 255,0,0


screen = pygame.display.set_mode(size)
# ball = pygame.image.load("cat.png")
# ball1 = pygame.image.load("catgirl.png")
# ballrect = ball.get_rect()
# ballrect1 = ball1.get_rect()
cur = time.time()


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
        val =  GPIO.input(26)
        print "hub: ", val, "node: ", context
        if val == 1:
            GPIO.output(13, GPIO.HIGH)
            #time.sleep(3)

            state = GPIO.input(26)
            if state == 1:
                val == 1
            else:
                continue
        else:
            GPIO.output(13, GPIO.LOW)

            time.sleep(0.2)
        
        # Pygame
        screen.fill(black)
        pygame.draw.rect(screen, white, (0, 0, 320, 25), 0)
        pygame.draw.rect(screen, white, (0, 95, 250, 50), 0)
        pygame.draw.rect(screen, white, (0, 240 - 25, 320, 25), 0)
        if val == 1:
            pygame.draw.circle(screen, red, (50,50), 20)
        if context == 1:
            pygame.draw.circle(screen, red, (150,50), 20)
	pygame.display.flip()


