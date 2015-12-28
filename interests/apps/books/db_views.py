# -*- coding: utf-8 -*-
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.db.models import Q
from apps.books.models import DouBanBook
from utils.log import logger
import requests
import json

from utils.constants import (
    success_res,
    invalid_query_res,
    request_error_res,
    value_error_res,
)

from utils.extra_tools import filter_book_info

BASE_API_URL = 'https://api.douban.com/v2/book/'


def get_book_by_id(request):
    """
    根据ID获取图书信息
    """
    book_id = request.REQUEST.get('book_id', None)
    if isinstance(book_id, str):
        request_id_url = BASE_API_URL + book_id
        book_info_rep = requests.get(request_id_url)
        if book_info_rep.status_code == 200:
            book_info = book_info_rep.json()
        else:
            return HttpResponse(request_error_res)
        q_data = {'book_id': book_id,
                  'isbn10': book_info.get('isbn10'),
                  'isbn13': book_info.get('isbn13')}
        book_query_set = DouBanBook.objects.filter(Q(**q_data))

        if book_query_set.exists():
            book_info = book_query_set.first().__dict__
            book = filter_book_info(book_info, book_id)
            logger.info(book)
        else:
            book = filter_book_info(book_info, book_id)
            try:
                DouBanBook.objects.create(**book)
            except Exception as e:
                logger.info(e)
                return HttpResponse(json.dumps(value_error_res))
        return HttpResponse(json.dumps(book))
    else:
        return HttpResponse(json.dumps(request_error_res))



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




