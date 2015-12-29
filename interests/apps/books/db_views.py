# -*- coding: utf-8 -*-
import json

from django.http import (
    HttpResponse
)
import requests

from utils.constants import (
    request_error_res,
)
from apps.books.utils.extra_tools import return_book_info


BASE_API_URL = 'https://api.douban.com/v2/book/'


def get_book_by_id(request):
    """
    根据ID获取图书信息
    """
    book_id = request.REQUEST.get('book_id', None)
    if isinstance(book_id, str):
        request_id_url = BASE_API_URL + book_id
        book_info_rep = requests.get(request_id_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))


def get_book_by_isbn(request):
    """
    根据ISBN获取图书信息
    """
    isbn = request.REQUEST.get('isbn', None)
    if isinstance(isbn, str):
        request_isbn_url = BASE_API_URL + 'isbn/' + isbn
        book_info_rep = requests.get(request_isbn_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))


def search_book_by_name(request):
    """
    根据书名搜索图书信息
    """
    book_name = request.REQUEST.get('book_name', None)
    if isinstance(book_name, str):
        request_book_name_url = BASE_API_URL + 'search/?q=' + book_name
        book_info_rep = requests.get(request_book_name_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))


def get_book_collect_by_uid(request):
    """
    根据用户ID获取某个用户的所有图书收藏信息
    """
    uid = request.REQUEST.get('uid', None)
    if isinstance(uid, str):
        request_collect_url = BASE_API_URL + 'user/' + uid + '/collections'
        book_info_rep = requests.get(request_collect_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))


def get_book_notes_by_id(request):
    """
    根据ID获取某本图书的所有笔记
    """
    book_id = request.REQUEST.get('book_id', None)
    if isinstance(book_id, str):
        request_notes_url = BASE_API_URL + book_id + '/annotations'
        book_info_rep = requests.get(request_notes_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))


def get_book_series_by_id(request):
    """
    根据ID获取丛书书目信息
    """
    book_id = request.REQUEST.get('book_id', None)
    if isinstance(book_id, str):
        request_series_url = BASE_API_URL + 'series/' + book_id + '/books'
        book_info_rep = requests.get(request_series_url)
        book_res = return_book_info(book_info_rep)
        return HttpResponse(json.dumps(book_res))
    else:
        return HttpResponse(json.dumps(request_error_res))




