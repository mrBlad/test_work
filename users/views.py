# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from forms import NewUserForm, UpdateUserForm


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


class Profile(View):
    template_name = 'profile.html'

    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('login')

        user = request.user

        print(user.confirm_file)

        path_to_file = str(user.confirm_file).split('/')[-1]

        initial = {'path_to_file': path_to_file}

        context = {
            'profile_form': UpdateUserForm(instance=request.user, initial=initial)
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if not request.user.is_authenticated():
            return redirect('login')

        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)

        if user_form.errors:
            print(user_form.errors)

        if user_form.is_valid():
            user = request.user
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            if user_form.cleaned_data['middle_name']:
                user.middle_name = user_form.cleaned_data['middle_name']
            user.birthday = user_form.cleaned_data['birthday']
            user.email = user_form.cleaned_data['email']
            user.confirm_file = user_form.cleaned_data['confirm_file']
            user.save()

            return redirect('home')

        context = {
            'profile_form': UpdateUserForm(instance=request.user)
        }

        return render(request, self.template_name, context)
