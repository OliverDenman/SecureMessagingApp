import eel
import socket
import sys
from EncryptData import *
from Functions import *
import random
import string

eel.init("HTML")

LocalIpV4 = socket.gethostbyname(socket.gethostname())
eel.GetIp(LocalIpV4)

def CreateServer(IpAddress, Port, logs, encrypt, anom):
    Error = CheckUserJoinCredentials(IpAddress, Port)
    print (Error)
    ErrorHandler(Error)


def ErrorHandler(error):
    eel.ErrorUpdater(error)() #Setting the error message for login

@eel.expose
def GetInputFromServer(IpAddress, Port, logs, encrypt, anom):
    try:
        CreateServer(IpAddress, Port, logs, encrypt, anom)
    except:
        UserJoin(IpAddress, Port, logs, encrypt, anom)

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
    print(IpAddress, Port, logs, encrypt, anom)

eel.start("index.html", size=(1200,800), mode="chrome", block=True)


def ServerStart():
    pass

#Hello, Test
# {
#     "auto_formatting": true,
#     "autoformat_ignore":
#     [
#     ],
#     "pep8_ignore":
#     [
#         "E501"
#     ],
#     "anaconda_linter_underlines": false,
#     "anaconda_linter_mark_style": "none",
#     "display_signatures": false,
#     "disable_anaconda_completion": true,
#     "python_interpreter": "/usr/local/bin/python3"
# }
