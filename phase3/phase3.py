import base64

import hashlib
import os
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import ast


class Phase3:

    def __init__(self):
        self.key1 = os.urandom(32)
        self.key2 = os.urandom(16)
        self.iv = random.randbytes(16)
        self.iv2 = random.randbytes(8)

    def encode(self, message: str):
        msg = base64.b64encode(bytes(message, encoding='utf8'))
        print(msg.decode())

    def decode(self, message: bytes):
        msg = base64.b64decode(message)
        print(msg.decode())

    def sha256(self, message: str):
        msg = hashlib.sha256(bytes(message, encoding='UTF-8')).hexdigest()
        return msg

    def md5(self, message: str):
        msg = hashlib.md5(bytes(message, encoding='UTF-8')).hexdigest()
        return msg

    def sha1(self, message: str):
        msg = hashlib.sha1(bytes(message, encoding='UTF-8')).hexdigest()
        return msg

    def getpasswordlist(self):
        with open("D:\Education\GL4\SEM1\AI\securityProject\phase3\passwords.txt", "r") as file:
            for i in file.readlines():
                yield (i)

    def craquagehash(self, hashmessage: str):
        print("choisir craq method: ")
        print("1-md5")
        print("2-sha1")
        print("3-sha256")
        x = 0
        while x not in [1, 2, 3]:
            x = int(input())
        for i in self.getpasswordlist():
            if x == 1:
                msg = self.md5(i[:-1])
            elif x == 2:
                msg = self.sha1(i[:-1])
            else:
                msg = self.sha256(i[:-1])
            if msg == hashmessage:
                print("word found: ", i)
                break
        print(f"\nCould Not find message in password list\n")

    def chiffrementaes(self, message: str):
        cipher = Cipher(algorithms.AES(self.key1), modes.CBC(self.iv))
        encryptor = cipher.encryptor()
        ct = encryptor.update(message.encode() + (b" " * (32 - (len(message) % 32)))) + encryptor.finalize()
        print(ct)
        file = open("output.txt", "wb")
        file.write(ct)

    def chiffrementdes(self, message: str):
        cipher = Cipher(algorithms.TripleDES(self.key2), modes.CBC(self.iv2))
        encryptor = cipher.encryptor()
        ct = encryptor.update(message.encode() + (b" " * (32 - (len(message) % 32)))) + encryptor.finalize()
        print(ct)
        file = open("output.txt", "wb")
        file.write(ct)

    def dechiffrementaes(self, path: str):
        file = open(path, 'rb')
        message = file.read()
        cipher = Cipher(algorithms.AES(self.key1), modes.CBC(self.iv))
        decryptor = cipher.decryptor()
        print((decryptor.update(message + (b"" * (32 - (len(message) % 32)))) + decryptor.finalize()).decode())

    def dechiffrementdes(self, path: str):
        file = open(path, 'rb')
        message = file.read()
        cipher = Cipher(algorithms.TripleDES(self.key2), modes.CBC(self.iv2))
        decryptor = cipher.decryptor()
        print((decryptor.update(message + (b"" * (16 - (len(message) % 16)))) + decryptor.finalize()).decode())