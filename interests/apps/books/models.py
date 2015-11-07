# -*- coding: utf-8 -*-
from django.db import models
from datetime import date


class Book(models.Model):
    today_str = date.today().isoformat()

    # rating
    numRaters = models.IntegerField(default='', blank=True, verbose_name='评价人数')
    average = models.DecimalField(default='', max_digits=9, decimal_places=2, blank=True, verbose_name='评分')

    subtitle = models.CharField(default='', max_length=128, blank=True, verbose_name='图书标题')
    author = models.CharField(default='', max_length=256, blank=True, verbose_name='作者')
    pubdate = models.DateField(blank=True, null=True, help_text=today_str, verbose_name='出版年')

    # tags
    tags = models.TextField(default='', blank=True, verbose_name='标签')

    origin_title = models.CharField(max_length=128, verbose_name='图书原始标题')
    book_image = models.URLField(default='', max_length=256, blank=True,
                                 verbose_name='图书封面')
    binding = models.CharField(default='', max_length=128, blank=True,
                               verbose_name='装帧')
    translator = models.CharField(default='', max_length=256, blank=True,
                                  verbose_name='翻译者')
    catalog = models.TextField(default='', blank=True,
                               verbose_name='目录')
    ebook_url = models.URLField(default='', max_length=256, blank=True,
                                verbose_name='电子图书')
    pages = models.SmallIntegerField(default=0, blank=True, null=True,
                                     verbose_name='页数')

    # images
    face_s = models.URLField(default='', max_length=256, blank=True,
                             verbose_name='小封面')
    face_m = models.URLField(default='', max_length=256, blank=True,
                             verbose_name='中封面')
    face_l = models.URLField(default='', max_length=256, blank=True,
                             verbose_name='大封面')
    alt = models.URLField(default='', max_length=256, blank=True,
                          verbose_name='访问地址')
    book_id = models.IntegerField(default='', blank=True, verbose_name='图书ID')
    isbn_10 = models.CharField(verbose_name='ISBN_10', default='', max_length=10, blank=True)
    isbn_13 = models.CharField(verbose_name='ISBN_13', default='', max_length=10, blank=True)
    publisher = models.CharField(default='', max_length=256, blank=True,
                                 verbose_name='出版社')
    title = models.CharField(default='', max_length=128, blank=True,
                             verbose_name='图书书名')
    url = models.URLField(default='', max_length=256, blank=True,
                          verbose_name='图书地址')
    author_intro = models.TextField(default='', blank=True,
                                    verbose_name='作者简介')
    summary = models.TextField(default='', blank=True,
                               verbose_name='内容简介')
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True,  null=True,
                                verbose_name='定价')
    ebook_price = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True,
                                      verbose_name='电子书定价')



