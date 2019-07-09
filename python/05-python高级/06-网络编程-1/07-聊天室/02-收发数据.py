from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("",7788))

while True:
    rese = input("你想干啥?")

    receData = udpSocket.recvfrom(1024)

    recData,recAddr = receData
    
    if recData.decode("gb2312")=='over':
        print("人家不想和你聊了")
        break

    print("[ip地址",recAddr[0],'端口号',recAddr[1],']',recData.decode("gb2312"))



