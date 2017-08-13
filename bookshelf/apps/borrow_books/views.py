# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import HttpResponse
import requests
import json

from services import borrowService as service
from .. import untils_


def load(request):
    appid = 'wxaab569c52de78bc3'
    appsecret = 'b1e31005610020ffb5311b5952ff00f6'
    code = request.GET['code']
    box_id = request.GET['state']
    with open('x.txt', 'w') as f:
        get_acces_tooken_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='+\
                               appid+'&secret='+appsecret+'&code='+code+'&grant_type=authorization_code'
        response = requests.get(get_acces_tooken_url).text
        f.write(response)
        openid = eval(response)['openid']
        f.write(openid)

    # return HttpResponse('openid:%s * box_id:%s' %(openid, box_id))
    oppen_id = openid

    #  验证是否存在oppen_id
    oppen_id_exits = service.verify_oppen_id(oppen_id)
    if oppen_id_exits:
        #  用户权限校验
        user_rights = service.user_rights_check(oppen_id, box_id)
        if user_rights == 'busyDoing':
            return HttpResponse("有任务.html")
        elif user_rights == 'outOfNum':
            return HttpResponse('超出可借数量')
        else:
            #  隔间状态校验
            box_status = service.box_status_(box_id, oppen_id)
            if box_status == 'exception':
                return HttpResponse('提示：被占用')
            elif box_status == 'door_unlock':
                return HttpResponse('提示：门没锁')
            elif box_status == 'book_none':
                return HttpResponse('提示：没有书在里面')
            else:
                #  开锁
                msg = service.unlock(box_status)
                if msg == '异常':
                    return HttpResponse('开锁出现异常')
                else:
                    return HttpResponse('ok unlock')

    else:
        return HttpResponse('注册.html')


def back_book_monitor(request):
    pass