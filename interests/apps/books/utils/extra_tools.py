# -*- coding: utf-8 -*-
import time
import json
from decimal import Decimal
from django.db.models import Q
from apps.books.models import DouBanBook
from utils.log import logger

from utils.constants import (
    success_res,
    invalid_query_res,
    request_error_res,
    value_error_res,
)


def return_book_info(book_info_rep, book_id=None):
    """返回book的信息"""
    if book_info_rep.status_code == 200:
        book_info = book_info_rep.json()
    else:
        return request_error_res
    q_data = {'isbn10': book_info.get('isbn10'),
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
            return value_error_res
    return book


def filter_book_info(book_info, book_id=None):
    """
    过滤查询数据
    """
    book = dict()
    try:
        book['numRaters'] = book_info.get('rating').get('numRaters')
        book['average'] = book_info.get('rating').get('average')
        book['face_s'] = book_info.get('images').get('small')
        book['face_m'] = book_info.get('images').get('medium')
        book['face_l'] = book_info.get('images').get('large')
    except:
        book['numRaters'] = book_info.get('numRaters')
        book['average'] = book_info.get('average')
        book['face_s'] = book_info.get('face_s')
        book['face_m'] = book_info.get('face_m')
        book['face_l'] = book_info.get('face_l')

    # pubdate = book_info.get('pubdate')
    # if hasattr(pubdate, 'isoformat'):
    #     pubdate = pubdate.isoformat()
    # book['pubdate'] = pubdate

    average = book.get('average')
    if isinstance(average, Decimal):
        average = "%.2f" % average
    book['average'] = average

    if book_id:
        book['book_id'] = book_id
    else:
        book['book_id'] = book_info.get('id')

    book_common = {
        'subtitle': book_info.get('subtitle'),
        'pubdate': book_info.get('pubdate'),
        'author': book_info.get('author'),
        'tags': book_info.get('tags'),
        'origin_title': book_info.get('origin_title'),
        'book_image': book_info.get('image'),
        'binding': book_info.get('binding'),
        'translator': book_info.get('translator'),
        'catalog': book_info.get('catalog'),
        'ebook_url': book_info.get('ebook_url'),
        'pages': book_info.get('pages'),
        'alt': book_info.get('alt'),
        'isbn10': book_info.get('isbn10'),
        'isbn13': book_info.get('isbn13'),
        'publisher': book_info.get('publisher'),
        'title': book_info.get('title'),
        'url': book_info.get('url'),
        'author_intro': book_info.get('author_intro'),
        'summary': book_info.get('summary'),
        'price': book_info.get('price'),
        'ebook_price': book_info.get('ebook_price')
        }
    book.update(book_common)
    return book
