from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.198.128",8899))
clientSocket.send("haha".encode("utf-8"))
#注意
#１．ｔｃｐ客户端已经链接好服务器，所以在以后的数据发送中不需要填写对方的ＩＰ和ｐｏｒｔ－－－打电话
#2.udp在发送数据的时候，因为没有之前的链接所以需要在每次的发送中，都要填写接受的ＩＰ和ＰＯＲＴ－－－发短信
recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData.decode('utf-8'))

clientSocket.close()


