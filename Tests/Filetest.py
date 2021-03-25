import pickle

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
        print (newDict)
        return newDict

username = "Ollie"
password = b'\xb2s\x05\x12z\xdae\xdb\x99\xc9\x13\xad\x88lZW'
#WriteToFile(username, password)
ReadFile()
