# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from forms import OrderForm
from models import Order, get_choices_label


def home_page(request):
    return render(request, "home_page.html")


def orders_page(request):
    if not request.user.is_authenticated():
        return redirect('login')

    user = request.user
    order_list = Order.objects.filter(user_id=user)

    for index, value in enumerate(order_list):
        order_list[index].status = get_choices_label(value.status)

    context = {'order_list': order_list}
    return render(request, "orders_page.html", context=context)


def order_page(request, pk):
    if not request.user.is_authenticated():
        return redirect('login')

    user = request.user
    order = Order.objects.filter(user_id=user, id=pk)

    for index, value in enumerate(order):
        order[index].status = get_choices_label(value.status)

    labels = {
        'id': 'Номер заказа',
        'user_full_name': 'Имя',
        'user_birthday': 'Дата рождения',
        'user_comment': 'Комментарий',
        'date_create': 'Дата формирования заказа',
        'date_finish': 'Дата готовности заказа',
        'status': 'Статус заказа'
    }

    context = {'order': order, 'labels': labels}

    return render(request, "order_info.html", context=context)


class CreateOrderView(View):
    template_name = 'order_page.html'

    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('login')

        if not request.user.last_name:
            return redirect('profile')

        user = request.user

        full_name = '{0} {1} {2}'.format(user.last_name, user.first_name, user.middle_name)
        initial = {'full_name': full_name, 'birthday': user.birthday, 'confirm_file': str(user.confirm_file)}

        order_form = OrderForm(initial=initial)

        context = {
            'order_form': order_form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if not request.user.is_authenticated():
            return redirect('login')

        if not request.user.last_name:
            return redirect('profile')

        user = request.user
        order_form = OrderForm(request.POST, instance=request.user)

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
            'order_form': OrderForm(initial=initial)
        }

        return render(request, self.template_name, context)
