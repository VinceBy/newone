from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(b"haha",("192.168.172.128",7788))

