# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render

from services import *


def list(request):

    res = book_list_service()
    return HttpResponse(res)


def detail(request):
    book_id = request.GET['id']
    res = book_detail_service(book_id)

    return HttpResponse(json.dumps(res))