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
    get_acces_tooken_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid='+\
                           appid+'&secret='+appsecret+'&code='+code+\
                           '&grant_type=authorization_code'
    response = requests.get(get_acces_tooken_url).text
    openid = eval(response)['openid']
    oppen_id = openid

    #  验证是否存在oppen_id
    oppen_id_exits = service.verify_oppen_id(oppen_id)
    if oppen_id_exits:
        #  用户权限校验
        user_rights = service.user_rights_check(oppen_id, box_id)
        if user_rights == 'busyDoing':
            with open('/var/www/bookshelf/static/account/unusual.html', 'r') as f:
                return HttpResponse(f)
        elif user_rights == 'outOfNum':
            with open('/var/www/bookshelf/static/account/over.html', 'r') as f:
                return HttpResponse(f)
        else:
            #  隔间状态校验
            box_status = service.box_status_(box_id, oppen_id)
            if box_status == 'exception' or box_status == 'door_unlock' or box_status == 'book_none':
                with open('/var/www/bookshelf/static/account/unusual.html', 'r') as f:
                    return HttpResponse(f)

            else:
                #  开锁
                msg = service.unlock(box_status)
                if msg == 'exception':
                    return HttpResponse('exception')
                else:
                    with open('/var/www/bookshelf/static/dist/userInfo.html', 'r') as f:
                        return HttpResponse(f)

    else:
        with open('/var/www/bookshelf/static/dist/register.html', 'r') as f:
            response = HttpResponse(f)
            # response.set_cookie("openid", oppen_id, 3600)
            return response


def back_book_monitor(request):
    pass