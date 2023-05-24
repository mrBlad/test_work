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

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<h1>Hello World!</h1>', html)
        self.assertTrue(html.endswith('</html>'))


class ServiceModelTest(TestCase):

    def test_service_model_upload_and_change(self):
        pass

#Создать модель сервисов
#Одним из сервисов является документы
#В зависимости от пользователя, страница динамически меняется
#Нужно проверить что в модель можно добавить новые сервисы
#Характеристики сервиса это: наименование, ссылка, краткое описание
#Изменять характеристики можно в панели админа