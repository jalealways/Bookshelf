# coding=utf-8

from .. import models


def handel_regist(obj):
    models.TbReaderInfo.objects.create(**obj)


def handel_login(obj):
    return models.TbReaderInfo.objects.filter(**obj)


def center_service(openid):
    obj = models.TbReaderInfo.objects.filter(open_id=openid)
    return {"tel": obj[0].tel_no,
            "borrow_num": obj[0].borrow_num,
            "start_time": obj[0].reg_time,
            "regist_address": ""}


def handel_eservation(openid, book_id):
    pass

