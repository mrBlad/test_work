# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from forms import NewUserForm


class Register(View):

    template_name = 'register.html'

    def get(self, request):
        context = {
            'register_form': NewUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('home')

        context = {
            'register_form': form
        }

        return render(request, self.template_name, context)
