from socket import *
from threading import Thread

#2.检测键盘，发数据
def send():
    while True:
        print("\r<<",end="")
        sendData = input("")
        udpSocket.sendto(sendData.encode("gb2312"),(destIp,destPort))

#1.收数据，然后打印
def receive():
    while True:
        print("\r>>",end="")
        receData = udpSocket.recvfrom(1204)
        content,destInfo = receData
        print(destInfo[0],content)

udpSocket = None
destIp = ''
destPort = 0

def main():
    
    global udpSocket
    global destIp
    global destPort

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    addPort = int(input("请输入本地的ｐｏｒｔ"))
    udpSocket.bind(("",addPort))

    destIp = input("请输入目的的ＩＰ：")
    destPort = int(input("请输入目的ｐｏｒｔ:"))

    tr = Thread(target=receive)
    ts = Thread(target=send)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__=="__main__":
    main()
