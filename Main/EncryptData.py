from Crypto.Cipher import AES #Type of encryption
from Crypto.Hash import SHA256 #Level of encryption


def encryption (data,password):

    data = data.ljust(16)

    IV = b'R\x80\xa5\xa2\x02{\xc8\x896\t\x85\x97G\xa3pO'

    Key = SHA256.new (password.encode('utf-8')).digest() #Making key from username

    encryptObj = AES.new(Key, AES.MODE_CBC, IV)
    cipher = encryptObj.encrypt(data.encode('utf-8'))

    return cipher
