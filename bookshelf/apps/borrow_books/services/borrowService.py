#coding=utf-8

import uuid
import time

from .. import models
from ... import untils_
from django.conf import settings


def verify_oppen_id(oppen_id):
    re = models.TbReaderInfo.objects.filter(open_id=oppen_id)
    if re.exists():
        return True
    else:
        return False


def user_rights_check(oppen_id, box_id):
    re = models.TbReaderInfo.objects.filter(open_id=oppen_id)
    if re[0].sessionid == '1':
        return 'busyDoing1'
    elif re[0].borrow_limit_num - re[0].borrow_num <= 0:
        return 'outOfNum'
    else:
        re.update(sessionid='1')
        return 'continue'


def box_status_(box_id, oppen_id):
    box = models.TbBookshelfBoxInfo.objects.filter(box_id=box_id)
    board_type, board_path, book_id, box_status, lock_status,  ray_status, \
    lock_board_id, lock_id, raspberry_ip, order_open_id = box[0].boardtype, box[0].lock_board_path, box[0].book_id, \
    box[0].box_status, box[0].lock_status, box[0].ray_status, \
    box[0].lock_board_id, box[0].lock_id, box[0].raspberry_ip, box[0].order_open_id

    obj = models.TbBookshelfBoxInfo.objects.filter(box_id=box_id)

    #  box_status  0 正常  1 被占用/异常
    if box_status == '1':
        obj.update(box_status='0')
        return 'exception'
    # elif cus_id != order_open_id:
    #     return 'n' + "别人预约"
    elif "unlock" == lock_status:
        obj.update(box_status='0')
        return "door_unlock"
    elif "0" == ray_status:
        obj.update(box_status='0')
        return "book_none"
    else:
        return [(board_type, board_path, lock_board_id, lock_id, 'unlock', "", ""),
                (board_type, board_path, lock_board_id, lock_id, 'check', "", ""),
                raspberry_ip]


def unlock(msg):
    redis_conn = untils_.RedisHelper(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    redis_conn.set(msg[2], str(msg[0]))
    # if back_msg == '异常？':
    #     models.TbBookshelfBoxInfo.objects.filter(box_id=msg[0]).update(box_status='1')
    #     models.TbReaderInfo.objects.filter(open_id=msg[4]).update(sessionid='0')
    #     return '异常'
    # else:
        #  还书状态监控
    # models.TbReaderInfo.objects.filter(open_id=msg[4]).update(sessionid='0')
    time.sleep(6)
    redis_conn.set(msg[2]+'check', str(msg[1]))
    time.sleep(3)
    back_msg = redis_conn.get(msg[2]+'checkback')
    return back_msg
