# -*- coding: utf-8 -*-
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
)
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import auth
import json
import time
from .forms import LoginForm
from utils.constant import (
    suc_res,
    invalid_query_res,
    request_error_res,
    value_error_res
)
from utils.log import logger


def login(request):
    """
    登录入口
    """
    return render_to_response('login.html')


def login_action(request):
    """
    用户验证
    """
    form = LoginForm(request.REQUEST)
    if not form.is_valid():
        return HttpResponse(invalid_query_res)
    username = form.cleaned_data.get('Username')
    password = form.cleaned_data.get('Password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        logger.info("user: {0} logined" .format(username))
        return render_to_response('index.html',suc_res)
    else:
        return render_to_response('login.html')


def logout(request):
    """
    登出
    """
    auth.logout(request)
    return render_to_response('login.html')


