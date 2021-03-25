import socket
from threading import *
import time

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
    try:
        while True:
            message = client.recv(Buffer)
            if message.decode("utf-8") != "quit":
                broadcast(message, username + ": ")
            else:
                client.send("Disconnecting".encode("utf-8"))
                client.close()
                del clients[client]
                broadcast(f"{username} has left the chat.".encode("utf-8"), "")
                break
    except:
        print ("DEBUG")
        pass

Buffer = 1024
addresses ={}
clients = {}
IP = socket.gethostname()
PORT = 1214

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))

if __name__ == "__main__":
    server.listen(5)
    connectionThread = Thread(target = ListenForConnections)
    connectionThread.start()
    connectionThread.join()
    server.close()
