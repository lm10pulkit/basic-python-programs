import socket

stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"

port =80

server_address = (server,port)

stream_socket.connect(server_address)

message = 'message'

stream_socket.sendall(message)

data = stream_socket.recv(10)

print(data)

print("socket closed")

stream_socket.close()