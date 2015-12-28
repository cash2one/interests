# -*- coding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)
from apps.books import db_views


urlpatterns = [
    url(r'^get_book_by_id/$', db_views.get_book_by_id),
]
