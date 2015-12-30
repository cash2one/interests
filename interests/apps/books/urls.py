# -*- coding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
)
from apps.books import db_views


urlpatterns = [
    url(r'^get_book_by_id/$', db_views.get_book_by_id),
    url(r'^get_book_by_isbn/$', db_views.get_book_by_isbn),
    url(r'^search_book_by_name/$', db_views.search_book_by_name),
    url(r'^get_book_collect_by_uid/$', db_views.get_book_collect_by_uid),
    url(r'^get_book_notes_by_id/$', db_views.get_book_notes_by_id),
    url(r'^get_book_series_by_id/$', db_views.get_book_series_by_id),
]
