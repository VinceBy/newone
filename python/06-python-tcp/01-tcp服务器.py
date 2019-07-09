from socket import *

severSocket = socket(AF_INET,SOCK_STREAM)

severSocket.bind(("",8899))

severSocket.listen(5)#表示最多的客户端

print("-------1--------")
clientSocket, clientInfo = severSocket.accept()

print("-------2--------")
#clientSocket表示这个新的客户端
#clientInfo 表示这个新的客户端的ｉｐ以及ｐｏｒｔ

recvData = clientSocket.recv(1024)

print("-------3--------")
print("%s:%s"%(str(clientInfo),recvData))

clientSocket.close()
severSocket.close()
