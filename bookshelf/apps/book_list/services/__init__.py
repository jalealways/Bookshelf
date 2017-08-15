#  coding=utf-8

from .. import models


def book_list_service():
    res = []
    books = models.TbBookBaseInfo.objects.all()

    for book in books:

        dic = {'id': book.isbn, 'imageURl': book.cover_pic,
               'title': book.book_name, 'author': book.author_name,
               'introduce': book.brief_introduction, 'publish': book.publishing_house,
               'type': 0}
        # dic['id'], dic['imageURL'], dic['title'],
        # dic['author'], dic['introduce'], dic['publish'],
        # dic['type'] = books[i].isbn, books[i].cover_pic,
        # books[i].book_name, books[i].author_name, books[i].brief_introduction,
        # books[i].publishing_house, books[i].original_proce
        res.append(dic)


    return res


def book_detail_service(id):
    book = models.TbBookBaseInfo.objects.filter(isbn=id)
    res_book = {'id': book[0].isbn, 'imageURl': book[0].cover_pic,
               'title': book[0].book_name, 'author': book[0].author_name,
               'introduce': book[0].brief_introduction, 'publish': book[0].publishing_house,
               'type': 0}

    return [res_book]

