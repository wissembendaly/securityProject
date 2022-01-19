import re   
from getpass import getpass
import bcrypt

from phase12.dbConnector import DbConnector

from phase12.User import User


class Phase12:
    
    db_connector= None   

    def __init__(self):
        self.dbConnector= DbConnector()

    def checkEmail(self,email:str):   
        #regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex= r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
        if(re.search(regex,email)):   
            return(True)   
        else:   
            print("email invalide\n")
            return(False)   
        
    def getEmail(self):
        email=str(input("veuillez saisir a valid email: "))
        while not(self.checkEmail(email)):
            email=str(input("veuillez saisir a valid email: "))
        return email

    def checkPassword(self, password:str):
        regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if(re.search(regex,password)):   
            return(True)   
        else:   
            print("password must contain atleast 8 characters, one letter and one number:\n")
            return(False)   

    def getPassword(self):
        password = getpass("veuillez saisir votre mot de passe: ")
        while not self.checkPassword(password):
            password = getpass()
        password2 = getpass("confirmer mot de passe: ")
        while not password==password2:
            password2=getpass("vueillez verifier votre mot de passe: ")
        return password


    def getNomPrenom(self,email: str):
        nom, prenom = email.split("@")[0].split(".")
        return nom,prenom
    
        
    def addUser(self, user:User):
        if(self.dbConnector.cursor.execute("SELECT * from user where email=%s",[user.email])==None):
            user.password=bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
            query = """INSERT INTO user (nom, prenom, email, password) 
                                VALUES 
                                (%s, %s, %s, %s) """
            self.dbConnector.cursor.execute(query,[user.nom,user.prenom,user.email,user.password])
            self.dbConnector.connection.commit()
            print(self.dbConnector.cursor.rowcount, "user added successfully")
        else:
            raise Exception("This user already exists please try another user")


    def registrate(self, email:str,password:str):
        query = "SELECT * FROM user where email = %s "
        self.dbConnector.cursor.execute(query,[email])
        user = self.dbConnector.cursor.fetchone()
        user1=User(user)
        matched = bcrypt.checkpw(password.encode(), user1.password.encode())
        if (matched):
            return user
        else:
            return None

    def signin(self):
        email= self.getEmail()
        print("veuillez saisir votre mot de passe: ")
        password = getpass()        
        return self.registrate(email,password)

    def signup(self):
        email = self.getEmail()
        password = self.getPassword()
        nom,prenom = self.getNomPrenom(email)
        user = User((None,nom,prenom,email,password))
        self.addUser(user)
        return user