#coding=utf-8
from .. import models


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
        return raspberry_id, box[0].box_id,



