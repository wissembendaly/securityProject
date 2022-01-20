import socket
import rsa
import json
import threading

from phase12.User import User
from phase12.phase12 import Phase12
from phase12.dbConnector import DbConnector


class Client:
    def __init__(self, port,user:User):

        self.host = '127.0.0.1'
        self.port = port
        self.active_users = {}
        self.user=user     



    def updatelistusers(self,users):
        self.active_users=users

    def receivemessages(self):
        while(True):
            response =json.loads(self.client.recv(1024).decode())
            if(response["content"]=="updatelisteusers"):
                self.updatelistusers(response["data"])
            else:
                data=response["data"]
                encryptedmessage=data["message"]
                message=rsa.decrypt(encryptedmessage,self.user.privatekey)
                sender=data["sender"]
                print("you received: ",message,"from:",sender)


    def startclient(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.client.connect((self.host, self.port))
        except Exception as e:
            print(e)
        self.client.send(str(self.user.id).encode())
        thread= threading.Thread(target=self.receivemessages,args=())
        thread.start()
        while(True):
            message= input("send message: ")
            if(message=="/disconnect"):
                self.client.send(message.encode())
                break
            else:
                print("choose receiver from this list:")
                for user in self.active_users:
                    print(user)
                destination=input()
                key=self.active_users[destination]
                encryptedmessage=rsa.encrypt(message,key)
                data=json.dumps({"destination":destination,"content":encryptedmessage})
                self.client.send(data.encode())



            # receiver=response["destination"]
            # message=response["content"]
#        if response["content"]=="/disconnect":
       # userslist= json.dump({"content":"updatelisteusers","data":{user:self.active_users[user][1] for user in self.active_users}})
