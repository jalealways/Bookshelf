# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals
from django.http import HttpResponse
from services import *


def back(request):
    book_id = request.GET('book_id')
    return search_book(book_id)
