import socket

def JoinSocket(IP,PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    ReceiveData(s)

def ReceiveData(s):
    while True:



IP = socket.gethostname()
PORT = 1236

JoinSocket(IP,PORT)
