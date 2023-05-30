# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
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
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('home')

        context = {
            'register_form': form
        }

        return render(request, self.template_name, context)


class Login(View):

    template_name = 'login.html'

    def get(self, request):
        context = {
            'login_form': AuthenticationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        context = {
            'login_form': form
        }

        return render(request, self.template_name, context)


def logout_request(request):
    logout(request)
    return redirect('home')


def profile_page(request):
    template_name = 'profile.html'

    return render(request, template_name)
