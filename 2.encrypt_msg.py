import base64
import hashlib
from Crypto.Cipher import AES 


BS = 16 #sets blocksize to 16byte (AES property)

# In AES, the blocksize has to be set to 128bit/16byte when message is passed to encrypt() function
# If the data input is not the multiple of the blocksize, then the padding proccess has to be done.
# Padding: A proccess that adds the block value at the end of the data input to match the multiple of the blocksize when it does not meet the condition 
pad = (lambda s: s+ (BS - len(s) % BS) * chr(BS - len(s) % BS).encode())
unpad = (lambda s: s[:-ord(s[len(s)-1:])])

class AESCipher(object):
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest() # a definition to apply hash to the using a ky to prevent it being exposed easily 
        print("AES Key(Key Cipher) : ", self.key)

    def encrypt(self, message): # a defnition to encrpy message using a key 
        message = message.encode() # encodes the message
        raw = pad(message) # pads the message that has the encoded
        cipher = AES.new(self.key, AES.MODE_CBC, self.__iv().encode('utf8')) # writes AES encryption algorithm then applies utf8
        enc = cipher.encrypt(raw) # AES encryption in place in place for padded message by using the algorithm
        return base64.b64encode(enc).decode('utf-8') # encodes base64 then returns the encrypted message

    def __iv(self):
        return chr(0) * 16

print("-"*100, "\n")
key = "aesKey"
msg = "Original Message."
print("AES KEY: ", key)
print("MESSAGE: ", msg)

aes = AESCipher(key) #creates instance of AESCipher to create 256bit hash applied key
# print(aes)

encrypt = aes.encrypt(msg) #encrpyts the message using the AES key
print("_"*100, "\n")
print("MESSAGE ENCRYPTION RESUILT USING AES KEY: ", encrypt)
print("_"*100, "\n")

