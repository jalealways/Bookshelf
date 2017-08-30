# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import json
import simplejson

from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .. import untils_
from services import *


def regist(request):

    openid = uuid.uuid4()
    id_ = request.COOKIES.get('openid')
    if id:
        openid = id_

    req = simplejson.loads(request.raw_post_data)
    password = req.get("password", 0)
    tel = req.get('tel', 0)
    if not password or not tel:
        return HttpResponse('wrong')
    obj = {"password": password,
           "tel_no": tel,
           "open_id": openid,
           "borrow_limit_num": 5,
           "borrow_num": 0,
           "order_num": 0,
           "active_time": datetime.datetime.now()}
    handel_regist(obj)

    return HttpResponse("ok")


def login(request):

    req = simplejson.loads(request.raw_post_data)
    tel = req.get('tel')
    password = req.get('password')
    if not password or not tel:
        return HttpResponse('wrong')
    obj = {"tel_no": tel,
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
        return HttpResponse(json.dumps(center_service(openid)))
    else:
        return HttpResponse('login_need')
