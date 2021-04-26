import pickle
import eel
import socket
from threading import *

Buffer = 1024
addresses ={}
clients = {}
# IP = socket.gethostname()
# PORT = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ListenForConnections(IP, PORT):
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

def initServerCreation(IP, PORT):
    PORT = int(PORT)
    server.bind((IP, PORT))
    server.listen(5)
    connectionThread = Thread(target = ListenForConnections, args=(IP,PORT));
    connectionThread.start()
    connectionThread.join()
    server.close()

def CharacterCheck(Data):
    count = 0
    bannedCharacters = ['"','!','£','$','%','^','&','*','(',')','-','+','=','[',']','{','}',':',';',"'",'#','~','/','.',',','>','<',' ']
    for _ in Data:
        for i in bannedCharacters:
            if _ == i:
                return True
    else:
        return False

def LoginCredentialsCheck(LoginUsername, LoginPassword):
    if "" in (LoginUsername):
        return "Please Enter a Username"
    elif "" in (LoginPassword):
        return "Please Enter a Password"

def SignUpCredentialsCheck(AccountCreationusername, AccountCreationpassword1, AccountCreationpassword2):
    if "" in (AccountCreationusername, AccountCreationpassword1, AccountCreationpassword2):
        return "Please Enter a Username and Password."
    elif CheckIfUsernameTaken(ReadFile(),AccountCreationusername) == True:
        return "Username Already Taken, Please Try Again."
    elif CharacterCheck(AccountCreationusername) == True:
        return "Special Characters Found, Please Try Again."
    elif len(AccountCreationusername) > 16: #Making sure that the password entered is less than 16 bit
        return "Username Too Long."
    elif len(AccountCreationpassword1) > 16:
        return "Password Too Long."
    elif len(AccountCreationpassword1) < 8:
        return "Password Too Short."
    elif AccountCreationpassword2 != AccountCreationpassword1: #Validating password
        return "Passwords Do No Match."
    else:
        return "Account Created"

def WriteToFile(username, password):
    Dict = ReadFile()
    Dict[username] = password
    with open("Data", "wb") as file:
        pickle.dump(Dict,file)
        file.close()

def ReadFile():
    with open("Data", "rb") as file:
        newDict = pickle.load(file)
        file.close()
        return newDict

def CheckIfUsernameTaken(Dict, username):
    if username in Dict:
        return True
    else:
        return False

def CheckUsernamePassword(username, password):
    Dict = ReadFile()
    if username in Dict:
        if Dict[username] == password:
            return True
        else:
            return "Password Incorrect."
    else:
        return False

def IpCheck(IpAddress):
    IpSplit = IpAddress.split(".")
    if len(IpSplit) != 4:
        return False
    for _ in IpSplit:
        try:
            if int(_) in range(0,255):
                next
            else:
                return False
        except:
            return False
    return True

def CheckUserJoinCredentials(IpAddress, port):
    if IpCheck(IpAddress) == False:
        return "Invalid Ip, Please Try Again"
    try:
        port = int(port)
        if len(port) > 5:
            return "Invalid Port, Please Try Again"
        if len(port) < 1:
            return "Invalid Port, Please Try Again"
        return "Connecting"
    except:
        return "Invalid Port, Please Try Again"


