# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from forms import LoginForm
from models import Account


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = Account.objects.filter(uid__exact=username, pwd__exact=password)
            if user:
                response = HttpResponseRedirect('/user/')
                response.set_cookie('elk_user_cookie', username, 360000)
                return response
            else:
                return HttpResponseRedirect('/user/login/')
    else:
        lf = LoginForm()
    return render(request, 'login.html', {'lf': lf})


def logout(request):
    response = HttpResponse('logout !!')
    response.delete_cookie('elk_user_cookie')
    return response


def register(request):
    response = HttpResponse('logout !!')
    response.delete_cookie('elk_user_cookie')
    return response

