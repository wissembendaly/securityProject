from phase12.User import User
from phase12.phase12 import Phase12

if __name__ == '__main__' :
    user : User= None
    phase12 = Phase12()

    while True:
        if not user:
            print("choisir un option:\n")
            print("1- créer un compte \n")
            print("2- se connecter\n")
            x=int(input())
            if(x==2):
                print(user.nom," ",user.prenom," connected")
            elif(x==1):
                y=phase12.getPassword()
                user = phase12.signup()
                print(user.nom," ",user.prenom," connected")
            else:
                print("option no valide\n")
        else:
            print("phase3\n")
            break