#coding=utf-8

from socket import *


def sender(ip, sendData):
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    serAddr = (ip, 7788)
    tcpClientSocket.connect(serAddr)
    tcpClientSocket.send(sendData)
    tcpClientSocket.close()

if __name__ == '__main__':
    sender('172.20.10.5', 'ok')
