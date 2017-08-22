
from socket import *
import redis

def sender(ip, sendData):
    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    serAddr = (ip, 7788)
    tcpClientSocket.connect(serAddr)
    tcpClientSocket.send(sendData)
    tcpClientSocket.close()


def get_box_status(msg_):
    pass


class RedisHelper():
    def __init__(self, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host, port)

    def get(self, key):
        if self.__redis.exists(key):
            msg = self.__redis.get(key, 0)
            self.__redis.delete(key)
            return msg
        else:
            return 0

    def set(self, key, value):
        self.__redis.set(key, value)


