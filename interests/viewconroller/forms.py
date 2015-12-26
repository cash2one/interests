# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='用户名')
    password = forms.CharField(required=True, label='密码')
