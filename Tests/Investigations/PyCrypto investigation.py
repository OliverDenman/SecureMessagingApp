from Crypto.Cipher import AES #Type of encryption
from Crypto.Hash import SHA256 #Level of encryption
from Crypto import Random #Random number

def encryption (Key, message, IV):

    blockSize = 16

    encryptObj = AES.new(Key, AES.MODE_CBC, IV)
    cipher = encryptObj.encrypt(message.encode('utf-8'))

    return cipher

def decrypt(Key, message, IV):

    blockSize = 16
    decryptObj = AES.new(Key, AES.MODE_CBC, IV)

    cipher = decryptObj.decrypt(message)
    return cipher

def getKey(password):
    hasher = SHA256.new (password.encode('utf-8'))
    return hasher.digest()

def Main():
    IV = Random.new().read(16)

    message = input("Please enter a message to encrypt: ")
    password = input("Please enter a password: ")
    en = encryption(getKey(password), message.ljust(16), IV)
    print(f"this is your message encrypted {en}")
    de = decrypt(getKey(password), en, IV)

    print(f"this is your message decrypted {de}")


if __name__ == '__main__':
    Main()


