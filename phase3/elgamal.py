import random
from math import pow


def pgcd(a,b):
    if a<b:
        return pgcd(b,a)
    elif a%b==0:
        return b
    else:
        return pgcd(b,a%b)

def gen_key(q):
    key= random.randint(pow(10,20),q)
    while pgcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c;
        y=(y*y)%c
        b=int(b/2)
    return x%c


class Elgamal:

    #For asymetric encryption
    def encryption(self,msg,q,h,g):
        ct=[]
        k=gen_key(q)
        s=power(h,k,q)
        p=power(g,k,q)
        for i in range(0,len(msg)):
            ct.append(msg[i])
        print("g^k used= ",p)
        print("g^ak used= ",s)
        for i in range(0,len(ct)):
            ct[i]=s*ord(ct[i])        
        return ct,p

    #For decryption
    def decryption(self,ct,p,key,q):
        pt=[]
        h=power(p,key,q)
        for i in range(0,len(ct)):
            pt.append(chr(int(ct[i]/h)))
        return pt

    def __init__(self):
        q=random.randint(pow(10,20),pow(10,50))
        g=random.randint(2,q)
        key=gen_key(q)
        h=power(g,key,q)
        self.q=q 
        self.key=key 
        self.h=h 
        self.g=g 
        print("g used=",self.g)
        print("g^a used=",self.h)

    def encrypt(self,message:str):
        ct,p=elgamal.encryption(message,self.q,self.h,self.g)
        return ct,p

    def decrypt(self,ct:str,p:str):
        pt=elgamal.decryption(ct,p,self.key,self.q)
        msg=''.join(pt)
        return msg

if __name__ == '__main__' :
    elgamal= Elgamal()
    message=input("Enter message:")
    ct,p=elgamal.encrypt(message)
    print("encrypted message :",ct)
    msg=elgamal.decrypt(ct,p)
    print("decrypted message: ",msg)
    


