# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from services import borrowService as service


def load(request):
    oppen_id = ''
    box_id = ''
    if oppen_id:
        return user_auth(oppen_id, box_id)
    else:
        return HttpResponse('index.html')


def user_auth(oppen_id, box_id):
    res = service.brow_num(oppen_id)
    if res == 'register':
        return HttpResponse('注册.html')
    elif res == 'duang':
        return HttpResponse('先把其他流程完成.html')
    else:
        borrow_num = res
        return box_status(box_id, oppen_id, borrow_num)


def box_status(box_id, oppen_id):
    res_msg = service.box_status(box_id, oppen_id)
    pass
    return res_msg

def unlock(request):
    pass


def back_book_monitor(request):
    pass