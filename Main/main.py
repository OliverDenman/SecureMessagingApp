import eel
import socket
import pickle
import sys
from EncryptData import *
from Functions import *
import random
import string
from threading import *
import os

eel.init("HTML")

LocalIpV4 = socket.gethostbyname(socket.gethostname())
eel.GetIp(LocalIpV4)

def CreateServer(IpAddress, Port, logs, encrypt, anom):
    Error = CheckUserJoinCredentials(IpAddress, Port)
    ErrorHandler(Error)
    serverCreationThread = Thread(target = initServerCreation, args=(IpAddress,Port));
    serverCreationThread.start()

def ErrorHandler(error):
    eel.ErrorUpdater(error)() #Setting the error message for login

@eel.expose
def CloseSocket():
    KillServer()
    os._exit(1)

@eel.expose
def CloseUser():
    KillUser()
    os._exit(1)

@eel.expose
def GetInputFromServerJoin(IpAddress, Port, logs, encrypt, anom):
    UserJoin(IpAddress, Port, logs, encrypt, anom)

@eel.expose
def GetInputFromServerCreate(IpAddress, Port, logs, encrypt, anom):
    CreateServer(IpAddress, Port, logs, encrypt, anom)

@eel.expose
def SignUp(username, password1, password2):
    ErrorCheck = SignUpCredentialsCheck(username, password1, password2)
    ErrorHandler(ErrorCheck)
    if ErrorCheck == "Account Created":
        enPass = encryption(password2, username) #Encrypting Password with the KEY of "username"
        WriteToFile(username, enPass)
        eel.GetUsername(username)()
        eel.ChangePage("userjoin.html")()


@eel.expose
def Login(username, password):
    ErrorCheck = LoginCredentialsCheck(username, password)
    ErrorHandler(ErrorCheck)
    enPass = encryption(password, username)
    passCheck = CheckUsernamePassword(username, enPass)
    if CheckIfUsernameTaken(ReadFile(),username) == False:
        ErrorHandler("Username Not Found, Please Try Again.")
    if passCheck == True:
        eel.GetUsername(username)()
        eel.ChangePage("userjoin.html")()
    if passCheck == "Password Incorrect.":
        ErrorHandler("Password Incorrect.")


@eel.expose
def Forgot(username):
    if CheckIfUsernameTaken(ReadFile(),username) == False:
        ErrorHandler("Username Not Found, Please Try Again.")
    else:
        newPassword = (''.join(random.choice(string.ascii_letters) for i in range(16)))
        eel.ForgotPasswordChangeNewPassword(newPassword)
        ErrorHandler("Password Changed.")
        enNewPassword = encryption(newPassword, username)
        WriteToFile(username,enNewPassword)

def UserJoin(IpAddress, Port, logs, encrypt, anom):
    Error = CheckUserJoinCredentials(IpAddress, Port)
    ErrorHandler(Error)
    userJoinThread = Thread(target = initUserJoin, args=(IpAddress,Port));
    userJoinThread.start()


eel.start("index.html", size=(1200,800), mode="chrome", block=True, port=8020)
