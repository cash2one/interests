# -*- coding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)
from viewconroller import views

urlpatterns = patterns('viewcontroller.views',
                       url(r'^login/$', views.login),
                       url(r'^logout/$', views.login_action),
                       url(r'^login_action/$', views.login_action)
                       )
