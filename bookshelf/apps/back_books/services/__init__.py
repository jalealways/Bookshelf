#coding=utf-8
from .. import models


def search_book(book_id):
    book_staus = models.TbBookStatusDetailHis.objects.filter(book_id=book_id)
    if book_staus:
        return handel_book_staus(book_staus)
    else:
        return 'not exists'


def handel_book_staus(book_staus):

    pass

