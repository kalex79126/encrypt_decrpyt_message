# Encrypt/Decrypt Messages with AES Key
This is a Python program that is designed to encrypt and decrypt a message using an AES key.
The Advanced Encryption Standard (AES), a.k.a. Rijndael is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.
This program uses a module called Crypto.Cipher which has a function for AES.

## Encryption
By using a key that has been hashed, it encrypts a message by following the proccesses below.
- Encode Message
- Apply Padding
- Apply utf8
- Encrypt Message
- Encode Base64
- Return
  
## Decryption
Decryption follows the opposite order of encryption.
- Decode Base64
- Apply utf8
- Decrypt Message
- Apply Unpadding
- Return
