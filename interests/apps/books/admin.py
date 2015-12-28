# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.books.models import (
    DouBanBook,
)


class DouBanBookAdmin(admin.ModelAdmin):
    list_display = ('numRaters', 'average', 'author', 'pubdate',
                    'pages', 'face_s', 'alt',
                    'book_id', 'isbn10', 'isbn13', 'publisher', 'title',
                    )

admin.site.register(DouBanBook, DouBanBookAdmin)
