from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

destIp = input("请输入目的的ＩＰ：")
destPort = int(input("请输入目的ｐｏｒｔ:"))
sendData = input("请输入要发送的数据:")

#udpSocket.sendto(sendData.encode("utf-8"),(destIp, destPort))
udpSocket.sendto(sendData.encode("gb2312"),(destIp, destPort))

