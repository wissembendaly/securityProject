class User:
    id:int
    nom:str
    prenom:str
    email:str
    password:str

    def __init__(self,params:tuple):
        (self.id,self.nom,self.prenom,self.email,self.password)=params



