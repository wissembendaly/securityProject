import codecs

import rsa

class Rsa:
    def __init__(self):
        (pubkey, privkey) = rsa.newkeys(512)    
        self.pubkey = pubkey
        self.privkey = privkey

    def encrypt(self,message: str):
        message = message.encode('utf8')
        encrypted_message = rsa.encrypt(message, self.pubkey)
        f = open("output.txt", "wb")
        f.write(encrypted_message)
        print(encrypted_message)
        return encrypted_message

    def decrypt(self, path: str):
        f = open(path, "rb")
        encryptedmessage = f.read()
        message = rsa.decrypt(encryptedmessage, self.privkey)
        print(message)
