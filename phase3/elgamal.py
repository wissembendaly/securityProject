import random
from math import pow


def pgcd(a, b):
    if a < b:
        return pgcd(b, a)
    elif a % b == 0:
        return b
    else:
        return pgcd(b, a % b)


def gen_key(q):
    key = random.randint(int(pow(10, 20)), q)
    while pgcd(q, key) != 1:
        key = random.randint(int(pow(10, 20)), q)
    return key


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x*y) % c
        y = (y*y) % c
        b = int(b/2)
    return x % c


class Elgamal:
    def __init__(self):
        q = random.randint(int(pow(10,20)), int(pow(10,50)))
        g = random.randint(2, q)
        key = gen_key(q)
        h = power(g, key, q)
        self.q = q
        self.key = key
        self.h = h
        self.g = g

    def encryption(self, msg, q, h, g):
        ct = []
        k = gen_key(q)
        s = power(h, k, q)
        p = power(g, k, q)
        for i in range(0, len(msg)):
            ct.append(msg[i])
        for i in range(0, len(ct)):
            ct[i] = s * ord(ct[i])
        return ct, p

    def decryption(self, ct, p, key, q):
        pt = []
        h = power(p, key, q)
        for i in range(0, len(ct)):
            pt.append(chr(int(ct[i] / h)))
        return pt

    def encrypt(self, message: str):
        ct, p = self.encryption(message, self.q, self.h, self.g)
        return ct, p

    def decrypt(self, ct, p):
        pt = self.decryption(ct,p,self.key,self.q)
        msg = ''.join(pt)
        return msg
    


