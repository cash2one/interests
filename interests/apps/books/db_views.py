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
        book_query_set = DouBanBook.objects.filter(
            **{'book_id': book_id,
               'isbn_10': book_info.get('isbn10'),
               'isbn_13': book_info.get('isbn13')})

        if book_query_set.exists():
            book = book_query_set.__dict__()
        if not book_query_set.exists():
            book = {
                'numRaters': book_info.get('rating').get('numRaters'),
                'average': book_info.get('rating').get('average'),
                'subtitle': book_info.get('rating').get('subtitle'),
                'author': book_info.get('author'),
                'pubdate': book_info.get('pubdate'),
                'tags': book_info.get('tags'),
                'origin_title': book_info.get('origin_title'),
                'book_image': book_info.get('image'),
                'binding': book_info.get('binding'),
                'translator': book_info.get('translator'),
                'catalog': book_info.get('catalog'),
                'ebook_url': book_info.get('ebook_url'),
                'pages': book_info.get('pages'),
                'face_s': book_info.get('images').get('small'),
                'face_m': book_info.get('images').get('medium'),
                'face_l': book_info.get('images').get('large'),
                'alt': book_info.get('alt'),
                'book_id': book_id,
                'isbn_10': book_info.get('isbn10'),
                'isbn_13': book_info.get('isbn13'),
                'publisher': book_info.get('publisher'),
                'title': book_info.get('title'),
                'url': book_info.get('url'),
                'author_intro': book_info.get('author_intro'),
                'summary': book_info.get('summary'),
                'price': book_info.get('price'),
                'ebook_price': book_info.get('ebook_price')
            }
            logger.info(book)
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




