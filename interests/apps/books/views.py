# -*- coding: utf-8 -*-
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.db.models import Q
from apps.books.models import Book
from utils.log import logger


def get_book_by_id(request):
    """
    根据ID获取图书信息
    """
    pass


def get_book_by_isbn(request):
    """
    根据ISBN获取图书信息
    """
    pass


def search_book_by_name(request):
    """
    根据书名搜索图书信息
    """
    pass


def get_book_collect_by_uid(request):
    """
    根据用户ID获取某个用户的所有图书收藏信息
    """
    pass


def get_book_notes_by_id(request):
    """
    根据ID获取某本图书的所有笔记
    """
    pass


def get_book_series_by_id(request):
    """
    根据ID获取丛书书目信息
    """
    pass




