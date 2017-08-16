# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render

from services import *


def book_list(request):
    type_ = request.GET['type']
    res = book_list_service(type_)
    return HttpResponse(json.dumps(res), content_type="application/json")


def detail(request):
    book_id = request.GET['id']
    res = book_detail_service(book_id)

    return HttpResponse(json.dumps(res), content_type="application/json")