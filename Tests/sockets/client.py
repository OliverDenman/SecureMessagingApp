import socket
from threading import *

def clientReceive():
    while True:
        try:
            message = clientSocket.recv(Buffer).decode("utf-8")
            print (message)
        except OSError:
            break

def clientSend():
    message = input("")
    clientSocket.send(message.encode("utf-8"))
    if message == "quit":
        print("Disconnecting")
        clientSocket.close()
        exit()

IP = socket.gethostname()
PORT = 1218

Buffer = 1024

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

clientReceiveThread = Thread(target=clientReceive)
clientReceiveThread.daemon = True
clientReceiveThread.start()

while True:
    clientSend()
