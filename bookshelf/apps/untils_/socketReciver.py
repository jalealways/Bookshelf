#coding=utf-8
from socket import *
from threading import Thread
from time import sleep

# 处理客户端的请求并执行事情
def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData)>0:
            print('recv[%s]:%s'%(str(destAddr), recvData))
        else:
            print('[%s]客户端已经关闭'%str(destAddr))
            break

    newSocket.close()


def main():

    serSocket = socket(AF_INET, SOCK_STREAM)

    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)

    localAddr = ('', 7788)

    serSocket.bind(localAddr)

    serSocket.listen(5)

    while True:


        newSocket,destAddr = serSocket.accept()

        client = Thread(target=dealWithClient, args=(newSocket,destAddr))
        client.start()


    serSocket.close()

if __name__ == '__main__':
    main()
