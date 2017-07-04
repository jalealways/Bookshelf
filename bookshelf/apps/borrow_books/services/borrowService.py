from .. import models
import uuid


def borrow_num(oppenid):
    re = models.TbReaderInfo.filter(wechat_id=oppenid)
    if re.exists():
        if re[0].sessionid:
            return 'duang'
        else:
            re.update(sessionid=uuid.uuid1())
            return re[0].borrow_limit_num - re[0].order_num
    else:
        return 'register'


def