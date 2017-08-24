# coding=utf-8

from .. import models


def handel_regist(obj):
    models.TbReaderInfo.objects.create(**obj)


def handel_login(obj):
    return models.TbReaderInfo.objects.filter(**obj)

