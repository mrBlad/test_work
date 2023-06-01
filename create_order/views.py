# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def home_page(request):
    return render(request, "home_page.html")


def order_page(request):
    return render(request, "order_page.html")

# Create your views here.
