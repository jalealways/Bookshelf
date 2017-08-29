# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .. import untils_
from services import *



def regist(request):

    openid = uuid.uuid4()
    # openid = request.COOKIES['openid']
    password = request.POST[u"password"]
    tel = request.POST[u'tel']
    obj = {"password": password,
           "tel_no": tel,
           "open_id": openid,
           "borrow_limit_num": 5,
           "borrow_num": 0,
           " order_num": 0,
           "active_time": datetime.datetime.now()}
    handel_regist(obj)

    return HttpResponse("ok")


def login(request):

    name = request.POST['tel']
    password = request.POST['password']
    obj = {"tel": name,
           "password": password}
    res = handel_login(obj)
    if res:
        response = HttpResponse("ok")
        response.set_cookie("openid", res[0].open_id, 3600)

        return response
    else:

        return HttpResponse("wrong")


def user_center(request):
    openid = request.COOKIES.get('openid', 0)
    if openid:
        return HttpResponse(center_service(openid))
    else:
        return HttpResponse('login_need')
