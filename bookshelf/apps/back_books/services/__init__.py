#coding=utf-8

from django.conf import settings

from .. import models
from ... import untils_

def search_book(book_id):
    book_ = models.TbBookshelfBoxInfo.filter(book_id=book_id)
    if book_:
        return book_id, book_.order_open_id
    else:
        return 0, 0


def reader_check(oppen_id):
    sessionid = models.TbReaderInfo.filter(open_id=oppen_id)[0].sessionid
    if sessionid == '1':
        return True
    else:
        models.TbReaderInfo.filter(open_id=oppen_id).update(sessionid='1')
        return False


def select_box(raspberry_id):
    box = models.TbBookshelfBoxInfo.filter(raspberry_id=raspberry_id,
                                           box_status='0',
                                           ray_status='0')
    if not box:
        return 'box_full'
    else:
        pass
        return (box[0].board_type, box[0].board_path,
                box[0].lock_board_id, box[0].lock_id,
                'unlock', '', ''), box[0].raspberry_ip


def unlock_box(unlock_msg):
    redis_conn = untils_.RedisHelper(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    redis_conn.set(unlock_msg[1], str(unlock_msg[0]))



