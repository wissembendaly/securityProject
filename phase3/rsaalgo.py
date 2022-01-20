
import rsa

class Rsa:
    def __init__(self):
        (pubkey, privkey) = rsa.newkeys(512)    
        self.pubkey=pubkey
        self.privkey=privkey
# with open('keys/pubkey.pem', 'wb') as f:
# #     f.write(pubkey.save_pkcs1('PEM'))
# with open('keys/privkey.pem', 'wb') as f:
#     f.write(privkey.save_pkcs1('PEM'))

    def encrypt(self,message:str):
        message=message.encode('utf8')
        encrypted_message=rsa.encrypt(message,self.pubkey)
        return(encrypted_message)

    def decrypt(self,encryptedmessage):
        message=rsa.decrypt(encryptedmessage,self.privkey)
        return message

if __name__ == '__main__' :
    rsaalgo = Rsa()
    message=input("saisir message: ")
    encrypted_message=rsaalgo.encrypt(message)
    print("The encrypted message is: ",encrypted_message)
    msg=rsaalgo.decrypt(encrypted_message)
    print("The message is: ",msg.decode('utf8'))
