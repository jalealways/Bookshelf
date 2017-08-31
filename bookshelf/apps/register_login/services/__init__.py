# coding=utf-8

from .. import models


def handel_regist(obj):
    models.TbReaderInfo.objects.filter(tel_no=obj["tel_no"]).delete()
    models.TbReaderInfo.objects.filter(open_id=obj["open_id"]).delete()
    models.TbReaderInfo.objects.create(**obj)


def handel_login(obj):
    return models.TbReaderInfo.objects.filter(**obj)


def center_service(openid):
    obj = models.TbReaderInfo.objects.filter(open_id=openid)
    return {"tel": obj[0].tel_no,
            "borrow_num": obj[0].borrow_num,
            "start_time": str(obj[0].reg_time),
            "regist_address": ""}


def handel_eservation(obj):
    models.TbBookStatusDetail.objects.create(**obj)


