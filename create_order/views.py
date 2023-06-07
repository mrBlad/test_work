# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from forms import CreateOrderForm, ChangingOrderForm
from models import Order, get_choices_label
from os import path
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages


def download(request, path_to_file):
    if not request.user.is_authenticated():
        messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
        return redirect('login')

    file_path = path.join(settings.MEDIA_ROOT, path_to_file)
    if path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + path.basename(file_path)
            return response
    raise Http404


def home_page(request):

    objects = [
        {
            'name': 'Заказ документов',
            'urls': 'add-order',
        },
        {
            'name': 'История заказов',
            'urls': 'user-orders',
        }
    ]
    if request.user.is_authenticated:
        if request.user.user_type == 'worker':
            objects = [
                {
                    'name': 'Заказы',
                    'urls': 'user-orders',
                },
                {
                    'name': 'Статистика заказов',
                    'urls': 'stats',
                }
            ]

    context = {'objects': objects}

    return render(request, "home_page.html", context)


def stats_page(request):
    if not request.user.is_authenticated():
        messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
        return redirect('login')

    return render(request, 'stats_page.html')


def list_orders_page(request):
    if not request.user.is_authenticated():
        messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
        return redirect('login')

    user = request.user

    if request.user.user_type == 'client':
        order_list = Order.objects.filter(user_id=user)
    else:
        order_list = Order.objects.all()

    for index, value in enumerate(order_list):
        order_list[index].status = get_choices_label(value.status)

    context = {'order_list': order_list}

    return render(request, "orders_page.html", context=context)


class UserOrderPage(View):
    template_user_name = 'user_order_info.html'
    template_worker_name = 'worker_order_info.html'
    labels = {
        'id': 'Номер заказа',
        'user_full_name': 'Имя',
        'user_birthday': 'Дата рождения',
        'user_comment': 'Комментарий',
        'date_create': 'Дата формирования заказа',
        'date_finish': 'Дата готовности заказа',
        'status': 'Статус заказа',
        'confirm_file': 'Файл',
    }

    def get(self, request, pk):
        if not request.user.is_authenticated():
            messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
            return redirect('login')

        user = request.user

        if user.user_type == 'client':

            order = Order.objects.filter(user_id=user, id=pk)

            for index, value in enumerate(order):
                order[index].status = get_choices_label(value.status)

            context = {'order': order, 'labels': self.labels}

            return render(request, self.template_user_name, context=context)

        elif user.user_type == 'worker':

            data = Order.objects.get(id=pk)

            order_form = ChangingOrderForm(initial={'status': data.status})

            context = {'order_form': order_form, 'user_data': data, 'labels': self.labels}

            return render(request, self.template_worker_name, context=context)

        return Http404

    def post(self, request, pk):
        if not request.user.is_authenticated():
            messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
            return redirect('login')

        if request.user.user_type != 'worker':
            raise Http404

        order = Order.objects.get(id=pk)
        order_form = ChangingOrderForm(request.POST)

        if order_form.is_valid():
            order.status = order_form.cleaned_data["status"]
            order.save()

            return redirect('user-orders')

        context = {
            'order_form': ChangingOrderForm(initial={'status': order.status})
        }

        return render(request, self.template_worker_name, context)


class CreateOrderView(View):
    template_name = 'order_page.html'

    def get(self, request):
        if not request.user.is_authenticated():
            messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
            return redirect('login')

        if request.user.user_type != 'client':
            raise Http404

        if not request.user.last_name:
            messages.info(request, 'Заполните профиль, прежде чем использовать систему!')
            return redirect('profile')

        user = request.user

        full_name = '{0} {1} {2}'.format(user.last_name, user.first_name, user.middle_name)
        initial = {'full_name': full_name, 'birthday': user.birthday, 'confirm_file': str(user.confirm_file)}

        order_form = CreateOrderForm(initial=initial)

        context = {
            'order_form': order_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if not request.user.is_authenticated():
            messages.info(request, 'Чтобы воспользоваться системой, необходимо авторизоваться!')
            return redirect('login')

        if request.user.user_type != 'client':
            raise Http404

        if not request.user.last_name:
            messages.info(request, 'Заполните профиль, прежде чем использовать систему!')
            return redirect('profile')

        user = request.user
        order_form = CreateOrderForm(request.POST, instance=request.user)

        if order_form.is_valid():
            order = Order()

            order.user_id = user
            order.user_full_name = order_form.cleaned_data['full_name']
            order.user_birthday = order_form.cleaned_data['birthday']
            order.user_comment = order_form.cleaned_data['comment']
            order.confirm_file = order_form.cleaned_data['confirm_file']
            order.save()

            return redirect('home')

        full_name = '{0} {1} {2}'.format(user.last_name, user.first_name, user.middle_name)
        initial = {'full_name': full_name, 'birthday': user.birthday, 'confirm_file': str(user.confirm_file)}

        context = {
            'order_form': CreateOrderForm(initial=initial)
        }

        return render(request, self.template_name, context)
