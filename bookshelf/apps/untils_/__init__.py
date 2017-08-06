
from socket import *


def sender(ip, sendData):
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    serAddr = (ip, 7788)
    tcpClientSocket.connect(serAddr)
    tcpClientSocket.send(sendData)
    tcpClientSocket.close()

def get_box_status(msg_):
    pass