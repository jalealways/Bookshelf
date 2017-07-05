# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from services import borrowService as service
from .. import untils_

def load(request):
    oppen_id = '1'
    box_id = 'box0000003'
    if oppen_id:
        return user_auth(oppen_id, box_id)
    else:
        return HttpResponse('index.html')


def user_auth(oppen_id, box_id):
    res = service.borrow_num(oppen_id)
    if res == 'register':
        return HttpResponse('注册.html')
    elif res == 'duang':
        return HttpResponse('等待其他操作完成.html')
    else:
        borrow_num = res
        return box_status(box_id, oppen_id, borrow_num)


def box_status(box_id, oppen_id, borrow_num):
    res_msg = service.box_Status(box_id, oppen_id)
    if isinstance(res_msg, basestring):
        return HttpResponse(res_msg)
    else:
        unlock(res_msg)
        return HttpResponse('开锁啦')


def unlock(msg):
    pass
    # untils_.sender(msg)


def handel_lock_back_msg(request):
    pass


def back_book_monitor(request):
    pass