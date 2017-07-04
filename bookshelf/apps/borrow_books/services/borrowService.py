from .. import models
import uuid


def borrow_num(oppen_id):
    re = models.TbReaderInfo.filter(wechat_id=oppen_id)
    if re.exists():
        if re[0].sessionid:
            return 'duang'
        else:
            re.update(sessionid=uuid.uuid1())
            return re[0].borrow_limit_num - re[0].order_num
    else:
        return 'register'


def box_status(box_id, oppen_id):
    box = models.TbBookshelfBoxInfo.filter(box_id=box_id)
    book_id, box_status, lock_status,  ray_status, \
    lock_board_id, lock_id, raspberry_ip, order_reader_id =  \
        box.book_id, box.box_status, box.lock_status,  \
        box.ray_status, box.lock_board_id, box.lock_id, \
        box.raspberry_ip, box.order_reader_id
    if box_status == '1':
        msg = "异常"
        return msg
    elif oppen_id != order_reader_id:
        return "别人预约"
    elif "unlock" == lock_status:
        return "门没锁"
    elif "0" == ray_status:
        return "书没了"
    else:
        return (box_id, "操作命令", lock_board_id, lock_id)