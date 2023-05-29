# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.http import HttpRequest
from create_order.views import home_page


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertTrue(html.title, "Test site")
        self.assertTrue(html.endswith('</html>'))



