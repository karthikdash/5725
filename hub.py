# ========================================================================
#  Hub Client Code
# ========================================================================
# This is the main program which runs on the pi connected to the piTFT
# It spawns listener threads to listen to each of the nodes and automatically
# respawned if either of them are killed due to inactive nodes
# Written by Karthik(kd453) and Chirag(cw844)

import RPi.GPIO as GPIO
import time
import socket
from threading import Thread
import pygame
import os
import time

# piTFT Env Paramaters

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()


# piTFT heat map initializations

size = width, height = 320, 240
speed = [2,2]
speed1 = [2,2]
black = 20,20,40
white = 255,255,255
blue = 0,0,255
red = 255,0,0


screen = pygame.display.set_mode(size)
cur = time.time()


# For receving data from the node
HOST = '0.0.0.0'
PORT = 10000
PORT = 10001

context0 = -1
context1 = -1
context2 = -1
context3 = -1

pos0 = (0,0)
pos1 = (0,0)
pos2 = (0,0)
pos3 = (0,0)

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


# ========================================================================
#  Listener Thread 1
# ========================================================================
# Receives data from node 1

class ListenThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    # ========================================================================
    #  Executes the listening protocol
    # ========================================================================

    def run(self):
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.bind((HOST, PORT))
        self.recvSocket.listen(0)
        conn, addr = self.recvSocket.accept()
        print(conn,addr)
        print('Connected by', addr)
        while True:
            data1 = conn.recv(1024)
            data = json.load(data1)
            if not data:
                break

            try:
                # Update the global variable
                global context0, context1, pos0, pos1

                context0 = int(data["node0"])
                context1 = int(data["node1"])
                pos0     = int(data["pos0"])
                pos1     = int(data["pos1"])

            except Exception as e:
                print e

        context0 = -2
# Spawn the thread in the background

thread = ListenThread()
thread.start()


class ListenThread1(Thread):
    def __init__(self):
        Thread.__init__(self)

    # ========================================================================
    #  Executes the listening protocol
    # ========================================================================

    def run(self):
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.bind((HOST, PORT1))
        self.recvSocket.listen(0)
        conn, addr = self.recvSocket.accept()
        print(conn,addr)
        print('Connected by', addr)
        while True:
            data1 = conn.recv(1024)
            data = json.load(data1)
            if not data:
                break

            try:
                # Update the global variable
                global context0, context1, pos0, pos1

                context2 = int(data["node0"])
                context3 = int(data["node1"])
                pos2     = int(data["pos0"])
                pos3     = int(data["pos1"])

            except Exception as e:
                print e
        context2 = -2

# Spawn the thread in the background

thread = ListenThread()
thread.start()




last = 0
while True:

        # Pygame init screen
        screen.fill(black)
        pygame.draw.rect(screen, white, (0, 0, 320, 25), 0)
        pygame.draw.rect(screen, white, (0, 95, 250, 50), 0)
        pygame.draw.rect(screen, white, (0, 240 - 25, 320, 25), 0)


        # ========================================================================
        #  Node 1: Pir 1
        # ========================================================================

        if context0 == 1:
            pygame.draw.circle(screen, red, pos0, 25)
            pygame.draw.circle(screen, red, pos0, 20)
            pygame.draw.circle(screen, red, pos0, 15)
            pygame.draw.circle(screen, red, pos0, 10)

        if context0 > -1:
            pygame.draw.circle(screen, green, pos0, 5)

        # ========================================================================
        #  Node 1: Pir 2
        # ========================================================================


        if context1 == 1:
            pygame.draw.circle(screen, red, pos1, 25)
            pygame.draw.circle(screen, red, pos1, 20)
            pygame.draw.circle(screen, red, pos1, 15)
            pygame.draw.circle(screen, red, pos1, 10)

        if context1 > -1:
            pygame.draw.circle(screen, green, pos1, 5)

        # ========================================================================
        #  Node 2: Pir 1
        # ========================================================================


        if context2 == 1:
            pygame.draw.circle(screen, red, pos2, 25)
            pygame.draw.circle(screen, red, pos2, 20)
            pygame.draw.circle(screen, red, pos2, 15)
            pygame.draw.circle(screen, red, pos2, 10)

        if context1 > -1:
            pygame.draw.circle(screen, green, pos2, 5)

        # ========================================================================
        #  Node 2: Pir 2
        # ========================================================================

        if context3 == 1:
            pygame.draw.circle(screen, red, pos3, 25)
            pygame.draw.circle(screen, red, pos3, 20)
            pygame.draw.circle(screen, red, pos3, 15)
            pygame.draw.circle(screen, red, pos3, 10)

        if context3 > -1:
            pygame.draw.circle(screen, green, pos3, 5)

        # ========================================================================
        #  Respawn thread 1
        # ========================================================================


        if context0 == -2:
            thread = ListenThread()
            thread.start()
            context0 = -1

        # ========================================================================
        #  Respawn thread 2
        # ========================================================================


        if context2 == -2:
            thread1 = ListenThread1()
            thread1.start()
            context2 = -1

	pygame.display.flip()


