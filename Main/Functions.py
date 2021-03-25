import pickle
import eel

def CharacterCheck(Data):
    count = 0
    bannedCharacters = ['"','!','£','$','%','^','&','*','(',')','-','+','=','[',']','{','}',':',';',"'",'#','~','/','.',',','>','<',' ']
    for i in Data:
        for a in bannedCharacters:
            if i == a:
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


#--------------------------------NEED TO FIX -----------------------------------------------------


def CheckPort(port):
    print (port)

def CheckUserJoinCredentials(IpAddress, port):
    print (port, IpAddress)
    if IpAddress.count(".") == 3:
        split = IpAddress.split(".")
        for i in range(len(split)):
            if len(split[i]) > 3 or len(split[i]) < 1:
                return "Please Enter a Valid IP"
            if len(split[i]) <= 3 or len(split[i]) >= 1:
                CheckPort(port)
                return "Connecting"


#--------------------------------NEED TO FIX -----------------------------------------------------


