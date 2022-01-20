from phase12.phase12 import Phase12
from phase3.chatroom.server import Server
import socket


phase12 = Phase12()
server= Server(400,phase12)
server.start_server()



