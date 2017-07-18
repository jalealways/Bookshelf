# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from django.http import HttpResponse

from .. import untils_
from services import test as service


def test(request):
    res = service.findISBN()
    data = request.GET['unlock']
    # untils_.sender('172.20.10.5', data)
    return HttpResponse(data)
