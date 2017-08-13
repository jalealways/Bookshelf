#coding=utf-8

import uuid
import time

from .. import models
from ... import untils_


def verify_oppen_id(oppen_id):
    re = models.TbReaderInfo.objects.filter(open_id=oppen_id)
    if re.exists():
        return True
    else:
        return False


def user_rights_check(oppen_id, box_id):
    re = models.TbReaderInfo.objects.filter(open_id=oppen_id)
    if re[0].sessionid == '1':
        return 'busyDoing'
    elif re[0].borrow_limit_num - re[0].borrow_num <= 0:
        return 'outOfNum'
    else:
        re.update(sessionid='1')
        return 'continue'


def box_status_(box_id, oppen_id):
    box = models.TbBookshelfBoxInfo.objects.filter(box_id=box_id)
    book_id, box_status, lock_status,  ray_status, \
    lock_board_id, lock_id, raspberry_ip, order_open_id = box[0].book_id, \
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
        return (box_id, "操作命令", lock_board_id, lock_id, oppen_id)


def unlock(msg):
    return 'ok'
    back_msg = untils_.sender('1', msg)
    if back_msg == '异常？':
        models.TbBookshelfBoxInfo.objects.filter(box_id=msg[0]).update(box_status='1')
        models.TbReaderInfo.objects.filter(open_id=msg[4]).update(sessionid='0')
        return '异常'
    else:
        #  还书状态监控
        time.sleep(600)
        models.TbReaderInfo.objects.filter(open_id=msg[4]).update(sessionid='0')
        msg_ = msg
        box_status__ = untils_.get_box_status(msg_)
        return 'ok'
