from phase12.User import User
from phase12.phase12 import Phase12
#from phase3.phase3 import Phase3

if __name__ == '__main__' :
    user : User= None
    phase12 = Phase12()
    # phase3 = Phase3() 
    # phase3.sha1("hello world")
    # phase3.md5("hello world")
    




    while True:
        if not user:
            print("choisir un option:\n")
            print("1- créer un compte \n")
            print("2- se connecter\n")
            x=int(input())
            if(x==1):
                user=phase12.signup()
                print(user.nom," ",user.prenom," connected")
            elif(x==2):
                user = phase12.signin()
                print(user.nom," ",user.prenom," connected")
            else:
                print("option no valide\n")
        else:
            print("phase3\n")
            break
    
    # encode decode
    # encoded=phase3.encode("hello world")
    # msg=phase3.decode(encoded)
