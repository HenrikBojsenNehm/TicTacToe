import socket
import sys
import threading
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class p2pHost:
    print('Host')

class p2pClient:
    print('Client')

    hostIp = str
    hostPort = int
    gameHost = (hostIp, hostPort)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 50001))
