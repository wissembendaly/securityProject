from phase12.User import User
from phase12.phase12 import Phase12
from phase3.phase3 import Phase3
from phase3.rsaalgo import Rsa
from phase3.elgamal import Elgamal
from phase3.chatroom.client import Client


if __name__ == '__main__':
    user = None
    phase12 = Phase12()
    phase3 = Phase3()
    rsa_tool = Rsa()
    elgamal_tool = Elgamal()
    p =''
    while True:
        if not user:
            print("choisir un option:\n")
            print("1- créer un compte \n")
            print("2- se connecter\n")
            x=int(input())
            if x == 1:
                user = phase12.signup()
                print(user.nom, " ", user.prenom, " connected")
            elif x == 2:
                user = phase12.signin()
                print(user.nom, " ", user.prenom, " connected")
            else:
                print("option no valide\n")
        else:
            print("""Chose an option : \n
            1- encode a message
            2- decode a message
            3- hash a message with md5
            4- hash a message with sha1
            5- hash a message with sha256
            6- crack a hashed message
            7- cipher a message with aes 
            8- decipher a message with aes
            9- cipher a message with des
            10- decipher a message with des
            11- cipher a message with rsa
            12- cipher a message with ElGamal
            13- decipher a message with rsa
            14- decipher a message with ElGamal
            15- secure chatroom
            """)
            option = int(input())
            if option == 1:
                message = input("message : ")
                phase3.encode(message)
            if option == 2:
                message = input("message : ")
                phase3.decode(message.encode())
            if option == 3:
                message = input("message : ")
                print(phase3.md5(message))
            if option == 4:
                message = input("message : ")
                print(phase3.sha1(message))
            if option == 5:
                message = input("message : ")
                print(phase3.sha256(message))
            if option == 6:
                message = input("message : ")
                phase3.craquagehash(message)
            if option == 7:
                message = input("message : ")
                phase3.chiffrementaes(message)
            if option == 8:
                message = input("message : ")
                phase3.dechiffrementaes(message)
            if option == 9:
                message = input("message : ")
                phase3.chiffrementdes(message)
            if option == 10:
                message = input("message : ")
                phase3.dechiffrementdes(message)
            if option == 11:
                message = input("message : ")
                rsa_tool.encrypt(message)
            if option == 12:
                message = input("message : ")
                elgamal_tool.encrypt(message)
            if option == 13:
                message = input("file path : ")
                rsa_tool.decrypt(message)
            if option == 14:
                nomber_chars = int(input("nomber of characters : "))
                ct = []
                for i in range(nomber_chars):
                    char = input("char = ")
                    ct.append(char)
                elgamal_tool.decrypt(ct, p)
            if option == 15:
                client = Client(('127.0.0.1', 127), user.nom)
                client.run()
    # encode decode
    # encoded=phase3.encode("hello world")
    # msg=phase3.decode(encoded)
