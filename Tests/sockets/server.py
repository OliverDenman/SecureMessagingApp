import socket
from threading import *

def ListenForConnections():
    while True:
        client, clientAddress = server.accept()
        print (f"A connection with {clientAddress} has been established.")
        client.send(f"A connection with the server {IP} has been established.".encode("utf-8"))
        addresses[client] = clientAddress
        Thread(target=clientHandle, args=(client,)).start()

def broadcast(message, prefix):
    for _ in clients:
        _.send(prefix.encode("utf-8") + message)

def clientHandle(client):
    username = client.recv(Buffer).decode("utf-8")
    broadcast(f"{username} has joined the server".encode("utf-8"), "")
    clients[client] = username
    while True:
        message = client.recv(Buffer)
        if len(message) == 0: break
        if message.decode("utf-8") != "quit":
            broadcast(message, username + ": ")
        else:
            client.close()
            del clients[client]
            broadcast(f"{username} has left the chat.".encode("utf-8"), "")
            break

Buffer = 1024
addresses ={}
clients = {}
IP = socket.gethostname()
PORT = 1217
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initServerCreation():
    # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((IP, PORT))
    server.listen(5)
    connectionThread = Thread(target = ListenForConnections)
    connectionThread.start()
    connectionThread.join()
    server.close()

initServerCreation()
