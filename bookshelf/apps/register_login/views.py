# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .. import untils_
from services import *

# Create your views here.


def handle_register(request):
    return HttpResponse(request.COOKIES['openid'])
