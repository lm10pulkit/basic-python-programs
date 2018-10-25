import socket
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= "localhost"
port =8080

sock.bind((host,port))
sock.listen(1)

print("waiting for a connection\n\n\n")

(connection,client) = sock.accept()

print("client  :"+client+"\n\n")
data = connection.recv(100)

print("recieved data :"+data)

if data:
    connection.send(data)
else:
    print("no data intended")

