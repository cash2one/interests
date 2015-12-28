# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    Username = forms.CharField(label='用户名')
    Password = forms.CharField(label='密码')
