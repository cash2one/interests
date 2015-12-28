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
from utils.constants import (
    success_res,
    invalid_query_res,
    request_error_res,
    value_error_res
)
from utils.log import logger
from viewcontroller.forms import LoginForm


def login(request):
    """
    用户验证
    """
    form = LoginForm(request.REQUEST)
    if form.is_valid():
        username = form.cleaned_data.get('Username')
        password = form.cleaned_data.get('Password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            logger.info("user: {0} logined" .format(username))
            return HttpResponse(json.dumps(success_res))
    return render_to_response('login.html')


def logout(request):
    """
    登出
    """
    auth.logout(request)
    return render_to_response('login.html')
    # return HttpResponseRedirect('/interests/login')

