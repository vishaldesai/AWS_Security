# Example to generate data key from KMS master key and then encrypt and decrypt data using data key.
# https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.AES-module.html
# AES symmetric cipher
# AES (Advanced Encryption Standard) is a symmetric block cipher standardized by NIST . It has a fixed data block size of 16 bytes. Its keys can be 128, 192, or 256 bits long.
# AES is very fast and secure, and it is the de facto standard for symmetric encryption.
#

import base64
import json
import boto3
from Crypto import Random
from Crypto.Cipher import AES


def encrypt_data(aws_data,Text):

    #Boto3 Connection
    kms = boto3.client('kms')
    #API to generate data key from master key
    key = kms.generate_data_key(KeyId=aws_data['key_id'],KeySpec='AES_256')
    #Separate out plain data key and encrypted data key
    keyPlain  = key['Plaintext']
    keyCipher = key['CiphertextBlob']

    #Encrypt data
    obj = AES.new(keyPlain, AES.MODE_CFB, b'This is an IV123')
    CipherText = obj.encrypt(Text)

    return CipherText, keyPlain

def decrypt_data(aws_data, TextEncrypted, keyPlain):
    
    #Decrypt Data
    obj = AES.new(keyPlain, AES.MODE_CFB, b'This is an IV123')
    Text = obj.decrypt(TextEncrypted)
    return Text


def main():

    aws_data = {
        'region': 'us-east-1',
        'key_id': '5998040d-2926-4ab4-82a3-ca59b49f4d18',
    }

    #Plain Data
    Text = b'Hello, World!'
    print("Plain Text is : " + str(Text))

    #Call encrypt function to generate data key and encrypt data
    TextEncrypted, keyPlain = encrypt_data(aws_data, Text)
    print("PlainKey is :" + str(base64.b64encode(keyPlain)))
    print("Encrypted Text is : " + str(TextEncrypted))

    #Call decrypt function to decrypt data using plain data key
    TextDecrypted = decrypt_data(aws_data, TextEncrypted, keyPlain)
    print("Decrypted Text is :" + str(TextDecrypted))

if __name__ == '__main__':
    main()
