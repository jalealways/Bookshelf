#  coding=utf-8

from .. import models


def book_list_service():
    res = []
    books = models.TbBookBaseInfo.objects.all()
    for i in range(0, len(books)):
        dic = {}
        dic['id'], dic['imageURL'], dic['title'],
        dic['author'], dic['introduce'], dic['publish'],
        dic['type'] = books[i].isbn, books[i].cover_pic,
        books[i].book_name, books[i].author_name, books[i].brief_introduction,
        books[i].publishing_house, books[i].original_proce
        res.append(dic)
    return res


def book_detail_service(id):
    book = models.TbBookBaseInfo.objects.filter(isbn=id)
    res_book = {}
    res_book['id'], res_book['imageURL'], res_book['title'],
    res_book['author'], res_book['introduce'] = book[0].isbn,
    book[0].cover_pic, book[0].book_name, book[0].author_name,
    book[0].brief_introduction

    return res_book

