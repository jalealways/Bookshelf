# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.http import HttpResponse
from service import borrowService as service
from .. import untils_



def load(request):
    oppen_id = ''
    if oppen_id:
        res = service.brow_num(oppen_id)
        if res == 'register':
            return HttpResponse('注册.html')
        elif res == 'duang':
            return HttpResponse('先把其他流程完成.html')
        else:
            return res
    else:
        return HttpResponse('index.html')

