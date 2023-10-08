# import base64
import hashlib
from Crypto.Cipher import AES 

class AESCipher(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest() # a definition to apply hash to the using a key to prevent it being exposed easily 
        print("AES Key(Key Cipher) : ", self.key)


print("-"*100, "\n")
key = "aesKey"
msg = "Original Message."
print("AES KEY: ", key)
print("MESSAGE: ", msg)


aes = AESCipher(key) # creates instance of AESCipher to create 256bit hash applied key
#print(aes)
