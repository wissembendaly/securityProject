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
    power = 0
    while True:
        if not user:
            print("choisir un option:\n")
            print("1- créer un compte \n")
            print("2- se connecter\n")
            x = int(input())
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
            1 - Encode / Decode a message to base64
            2 - Hash a message / Crack a hashed message
            3 - Cipher / Decipher a message (Symmetric Algorithms)
            4 - Cipher / Decipher a message (Asymmetric Algorithms)
            5 - Chatroom
            """)
            option = int(input("Option = "))
            if option == 1:
                print("""\n what Option do you like
                1- encode a message
                2- decode a message 
                """)
                option1 = int(input("Option = "))
                if option1 == 1:
                    message = input("message : ")
                    phase3.encode(message)
                elif option1 == 2:
                    message = input("message : ")
                    phase3.decode(message.encode())
                else:
                    print("invalid Option")

            elif option == 2:
                print("""\n what Option do you like
                1- hash a message with md5
                2- hash a message with sha1
                3- hash a message with sha256
                4- crack a hashed message
                """)
                option2 = int(input("Option = "))
                if option2 == 1:
                    message = input("message : ")
                    print(phase3.md5(message))
                elif option2 == 2:
                    message = input("message : ")
                    print(phase3.sha1(message))
                elif option2 == 3:
                    message = input("message : ")
                    print(phase3.sha256(message))
                elif option2 == 4:
                    message = input("message : ")
                    phase3.craquagehash(message)
                else:
                    print("invalid Option")
            elif option == 3:
                print("""\n what option do you like
                1- cipher a message with AES 
                2- decipher a message with AES from a file
                3- cipher a message with DES
                4- decipher a message with DES from a file
                """)
                option3 = int(input("Option = "))
                if option3 == 1:
                    message = input("message : ")
                    phase3.chiffrementaes(message)
                elif option3 == 2:
                    path = input("file path : ")
                    phase3.dechiffrementaes(path)
                elif option3 == 3:
                    message = input("message : ")
                    phase3.chiffrementdes(message)
                elif option3 == 4:
                    path = input("file path : ")
                    phase3.dechiffrementdes(path)
                else:
                    print("invalid Option")
            elif option == 4:
                print(""" \n Chose an option:
                1- Cipher a message with RSA
                2- Decipher a message with RSA from a file
                3- Cipher a message with ElGamal
                4- Decipher a message with ElGamal
                """)
                option4 = int(input("Option = "))
                if option4 == 1:
                    message = input("message : ")
                    rsa_tool.encrypt(message)
                elif option4 == 2:
                    message = input("file path : ")
                    rsa_tool.decrypt(message)
                elif option4 == 3:
                    message = input("message : ")
                    _, power = elgamal_tool.encrypt(message)
                elif option4 == 4:
                    nomber_chars = int(input("nomber of characters : "))
                    ct = []
                    for i in range(nomber_chars):
                        char = input("char = ")
                        ct.append(char)
                    elgamal_tool.decrypt(ct, str(power))
                else:
                    print("INVALID OPTION")
            elif option == 5:
                client = Client(('127.0.0.1', 127), user.nom)
                client.run()
            else:
                print('invalid option')
