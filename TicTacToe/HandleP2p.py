import socket
import sys
import threading
import tkinter as tk
from tkinter import *
from tkinter import messagebox

hostIp = str
hostPort = int
clientPort = int

class p2pHost:
    print('Host')

class p2pClient:
    print('Client')


    print('Connect to rendezvous server')

    hostIp = input('Ip > ')
    hostPort = int(input('Port > '))
    
    gameHost = (hostIp, hostPort)

    #Connect to host
    #----------------------------------------------------------------
    # connect to rendezvous
    print('connecting to rendezvous server')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 50001))
    sock.sendto(b'0', gameHost)

    while True:
        data = sock.recv(1024).decode()

        if data.strip() == 'ready':
            print('checked in with server, waiting')
            break

    data = sock.recv(1024).decode()
    hostIp, clientPort, hostPort = data.split(' ')
    clientPort = int(clientPort)
    hostPort = int(hostPort)

    # punch hole
    print('punching hole')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', clientPort))
    sock.sendto(b'0', (hostIp, hostPort))

    print('ready to exchange messages\n')

    # listen for messages
    def listen(clientPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('0.0.0.0', clientPort))

        while True:
            data = sock.recv(1024)
            print('\rpeer: {}\n> '.format(data.decode()), end='')

    listener = threading.Thread(target=listen, args=(clientPort,), daemon=True);
    listener.start()

    # send messages
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', hostPort))

    while True:
        msg = input('> ')
        sock.sendto(msg.encode(), (hostIp, hostPort))