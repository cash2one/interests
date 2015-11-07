# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Book,
)


class BookAdmin(admin.ModelAdmin):
    list_display = ('numRaters', 'average', 'author', 'pubdate', 'tags', 'book_image', 'binding', 'translator',
                    'ebook_url', 'pages' ,'face_s', 'alt', 'isbn_10', 'isbn_13', 'publisher', 'title',
                    'author_intro', 'summary', 'price', 'ebook_price')

admin.site.register(Book, BookAdmin)
