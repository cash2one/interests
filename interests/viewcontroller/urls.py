# -*- coding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
    include,
)
from viewcontroller import views


urlpatterns = patterns('viewcontroller.views',
                       url(r'^login/$', views.login),
                       url(r'^logout/$', views.logout),
                       url(r'^index/$', views.index),
                       )

urlpatterns += [
    url(r'^book/?', include('apps.books.urls')),
    ]