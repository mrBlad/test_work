# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<html><h1>Hello World!</h1></html>')

# Create your views here.
