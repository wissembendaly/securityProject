import cryptography
import base64
from cryptography.hazmat.primitives import hashes
import hashlib
from Crypto import Random
from Crypto.Cipher import AES, DES

class Phase3:

    def encode(self,message:str):
        msg= base64.b64encode(bytes(message, encoding='utf8'))
        print(msg)
        return msg

    def decode(self,message:bytes):
        msg= base64.b64decode(message)
        print(msg)
        return msg

    def sha256(self,message:str):
        msg= hashlib.sha256(bytes(message,encoding='UTF-8')).hexdigest()        
        return msg

    def md5(self,message:str):
        msg= hashlib.md5(bytes(message,encoding='UTF-8')).hexdigest()
        return(msg)

    def sha1(self,message:str):
        msg= hashlib.sha1(bytes(message,encoding='UTF-8')).hexdigest()
        return(msg)

    def getpasswordlist():
        with open("./passwords.txt", "r") as file:
            for i in file.readlines():
                yield (i)

    def craquagehash(self,hashmessage:str):
        print("choisir craq method:")
        print("1-md5")
        print("2-sha1")
        print("3-sha256")
        x=0;
        while not x in [1,2,3]:
            x=int (input())
        for i in self.getpasswordlist():
            if(x==1):
               msg=self.md5(i)
            elif(x==2):
               msg=self.sha1(i)
            else:
               msg=self.sha256(i)
            if msg == hashmessage:
                return i
        print(f"\nCould Not find message in password list\n")

    key = 'abcdefghijklmnop'

    def chiffrementaes(self,message:str):
        iv_AES = Random.new().read(AES.block_size)
        aese = AES.new(self.key, AES.MODE_CFB, iv_AES)
        msg = aese.encrypt(message)
        return msg

    def chiffrementdes(self,message:str):
        iv_DES = Random.new().read(DES.block_size)
        dese = DES.new(self.key, DES.MODE_CFB, iv_DES)
        msg = dese.encrypt(message)

    def chiffrementsym(self,message:str):
        print("choisir methode de chiffrement:")
        print("1-AES")
        print("2-DES")
        x=0;
        while not x in [1,2]:
            x=int (input())
        if(x==1):
            return self.chiffrementaes(message)
        else:
            return self.chiffrementdes(message)
        


    def dechiffrementaes(self,hashmessage:str):
        iv_AES = Random.get_random_bytes(8)
        aesd = AES.new(self.key, AES.MODE_CFB, iv_AES)
        msg = aesd.decrypt(hashmessage)
        return msg


    def dechiffrementdes(self,hashmessage:str):
        iv_DES = Random.new().read(DES.block_size)
        desd = DES.new(self.key, DES.MODE_CFB, iv_DES)
        msg = desd.decrypt(hashmessage)
        return msg
    
    def dechiffrementsym(self,message:str):
        print("choisir methode de chiffrement:")
        print("1-AES")
        print("2-DES")
        x=0;
        while not x in [1,2]:
            x=int (input())
        if(x==1):
            return self.dechiffrementaes(message)
        else:
            return self.dechiffrementdes(message)
        