import rsa

class User:
    id:int
    nom:str
    prenom:str
    email:str
    password:str

    def __init__(self,params:tuple):
        (self.id,self.nom,self.prenom,self.email,self.password)=params

    def generatekeys(self):
        (pubkey,privatekey) = rsa.newkeys(512)
        self.privatekey=privatekey
        self.pubkey=pubkey
        return pubkey

