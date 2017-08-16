#  coding=utf-8

from .. import models


def book_list_service(type_):
    res = []
    # dim = models.TbDimBookClass.objects.filter(child_class_id=type_)
    # books = dim.TbBookBaseInfo.filter(status=1)
    books = models.TbBookBaseInfo.objects.filter(status=1, child_class=type_)

    for book in books:

        dic = {'id': unicode(book.isbn),
               'imageURL': 'http://www.read135.com' + unicode(book.cover_pic).encode('utf-8')[1:39],
               'title': unicode(book.book_name), 'author': unicode(book.author_name),
               'introduce': unicode(book.brief_introduction),
               'publish': unicode(book.publishing_house.publishing_house_name),
               'type': unicode(book.child_class.child_class)}
        # dic['id'], dic['imageURL'], dic['title'],
        # dic['author'], dic['introduce'], dic['publish'],
        # dic['type'] = books[i].isbn, books[i].cover_pic,
        # books[i].book_name, books[i].author_name, books[i].brief_introduction,
        # books[i].publishing_house, books[i].original_proce
        res.append(dic)

    return res


def book_detail_service(id):
    book = models.TbBookBaseInfo.objects.filter(isbn=id)
    res_book = {'id': unicode(book[0].isbn),
                'imageURL': 'http://www.read135.com' + unicode(book[0].cover_pic).encode('utf-8')[41:],
                'title': unicode(book[0].book_name), 'author': unicode(book[0].author_name),
                'introduce': unicode(book[0].brief_introduction),
                'publish': unicode(book[0].publishing_house.publishing_house_name),
                'type': 0}

    return res_book

