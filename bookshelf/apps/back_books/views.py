# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals
from django.http import HttpResponse
from services import *


def back(request):
    book_id = request.GET('book_id')
    raspberry_id = request.GET('raspberry_id')

    #  初始化还书任务
    book_status, oppenid = search_book(book_id)
    if book_status:
        # reader_status = reader_check(oppenid)
        # if reader_status:
        #     return HttpResponse('user_busyDoing')
        # 分配格间
        unlock_msg = select_box(raspberry_id)
        # unlock
        unlock_box(unlock_msg)
        return 'please_back_book'

    else:
        return HttpResponse('no_book_msg')
