# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.template import Template,Context

def index(request):
    return HttpResponse("Hello!")