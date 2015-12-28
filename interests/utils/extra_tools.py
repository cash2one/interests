# -*- coding: utf-8 -*-
import time
import json
from decimal import Decimal
from utils.log import logger


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
        'book_id': book_id,
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
