# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
from django.http import HttpResponse


def handle(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']
    token = "123456"

    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print "handle/GET func: hashcode, signature: ", hashcode, signature
    if hashcode == signature:
        return HttpResponse(echostr.encode('utf-8'))
    else:
        return HttpResponse('')


