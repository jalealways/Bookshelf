#coding=utf-8
from .. import models
import uuid


def borrow_num(oppen_id):
    re = models.TbReaderInfo.objects.filter(open_id=oppen_id)
    if re.exists():
        if re[0].sessionid:
            return 'duang'
        else:
            # re.update(sessionid=oppen_id)
            return re[0].borrow_limit_num - re[0].order_num
    else:
        return 'register'


def box_Status(box_id, oppen_id):
    box = models.TbBookshelfBoxInfo.objects.filter(box_id=box_id)
    book_id, box_status, lock_status,  ray_status, \
    lock_board_id, lock_id, raspberry_ip, order_open_id = box[0].book_id, \
    box[0].box_status, box[0].lock_status, box[0].ray_status, \
    box[0].lock_board_id, box[0].lock_id, box[0].raspberry_ip, box[0].order_open_id

    if box_status != '0':
        return box_status
    # elif cus_id != order_open_id:
    #     return 'n' + "别人预约"
    elif "unlock" == lock_status:
        return "门没锁"
    elif "0" == ray_status:
        return "书没了"
    else:
        return (box_id, "操作命令", lock_board_id, lock_id)
