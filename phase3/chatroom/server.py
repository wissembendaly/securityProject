from cryptography.hazmat.primitives import serialization
import socket
import rsa
import threading
import json

from phase12.User import User
from phase12.phase12 import Phase12
from phase12.dbConnector import DbConnector


class Server:
    def __init__(self, port,part1:Phase12):

        self.host = '127.0.0.1'
        self.port = port
        self.active_users = {}
        self.dbconnector:DbConnector = part1.dbConnector


    def getpublickey(self,id):
        query = "select pubkey from publickeys where userid= %s"
        self.dbconnector.cursor.execute(query, [id])
        (k,) = self.dbconnector.cursor.fetchone()
        byted_k = bytes(k, encoding="utf-8")
        #data = serialization.load_pem_public_key(byted_k)
        return byted_k

    def broadcast(self,msg:str):
        for id in self.active_users:
            self.active_users[id][0].send(msg.encode())
        print(msg)


    def inituser(self,connexion):
        print("user connected")    
        username = connexion.recv(1024).decode() 
        self.active_users [username] = (connexion,self.getpublickey(username))
        self.broadcast(' New person joined the room. Username: '+username)
        self.sendlistusers()
        return username

    def sendlistusers(self):
        dumped_date = {
            "content": "updatelisteusers",
            "data": {user: self.active_users[user][1] for user in self.active_users}
        }
        print(dumped_date)
        userslist = json.dumps(dumped_date)
        for user in self.active_users:
            self.active_users[user][0].send(userslist.encode())

    def start_server(self):        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("server started ")
        self.clients = []
        self.s.bind((self.host, self.port))
        self.s.listen(100)
        print("server listening on port: ",self.port)
        while (True):
            connexion, addr = self.s.accept()
            thread=threading.Thread(target=self.listentoclient,args=(connexion,))       
            thread.start()

    
    def disconnect(self,username):
        del(self.active_users[username])
        self.broadcast(username," disconnected")
        self.sendlistusers()

    def sendmessage(self,sender,receiver,message):
        content=json.dumps({"content":"message","data":{"sender":sender,"message":message}})
        self.active_users[receiver][0].send(content.encode())

    def listentoclient(self,connexion):
        username=self.inituser(connexion)
        while (True):
            response= json.loads(connexion.recv(1024).decode())
            if response["content"]=="/disconnect":
                self.disconnect(username)
                connexion.close()
            else:
                sender=username
                receiver=response["destination"]
                message=response["content"]
                self.sendmessage(sender,receiver,message)

