from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

class User:
    id:int
    nom:str
    prenom:str
    email:str
    password:str

    def __init__(self, params:tuple):
        (self.id,self.nom,self.prenom,self.email,self.password)=params

    def generatekeys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        self.privatekey = private_key
        # self.pubkey = pubkey
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        return pem.decode('utf-8')
