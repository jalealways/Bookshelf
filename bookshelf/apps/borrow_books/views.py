# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse

from services import borrowService as service
from .. import untils_


def load(request):
    x = request.GET['code']
    with open('x.txt', 'w') as f:
        f.write(x)
    return HttpResponse(x)
#     oppen_id = '1'
#     box_id = 'box0000003'
#
#     #  验证是否存在oppen_id
#     oppen_id_exits = service.verify_oppen_id(oppen_id)
#     if oppen_id_exits:
#         #  用户权限校验
#         user_rights = service.user_rights_check(oppen_id, box_id)
#         if user_rights == '有任务正在进行':
#             return HttpResponse("有任务.html")
#         elif user_rights == '超出可借数量':
#             return HttpResponse('超出可借数量')
#         else:
#             #  隔间状态校验
#             box_status = service.box_status_(box_id, oppen_id)
#             if box_status == '被占用':
#                 return HttpResponse('提示：被占用')
#             elif box_status == '门没锁':
#                 return HttpResponse('提示：门没锁')
#             elif box_status == '书没了':
#                 return HttpResponse('提示：没有书在里面')
#             else:
#                 #  开锁
#                 msg = service.unlock(box_status)
#                 if msg == '异常':
#                     return HttpResponse('开锁出现异常')
#                 else:
#                     return 'ok'
#
#     else:
#         return HttpResponse('注册.html')
#
#
# def back_book_monitor(request):
#     pass