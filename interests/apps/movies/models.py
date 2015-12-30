# -*- coding: utf-8 -*-
from django.db import models


class DouBanMovie(models.Model):

    movie_id = models.CharField(default='', max_length=20, blank=True,
                                verbose_name='条目id', primary_key=True)
    title = models.CharField(default='', max_length=256, blank=True,
                             verbose_name='中文名')
    original_title = models.CharField(default='', max_length=256, blank=True,
                                      verbose_name='原名')
    aka = models.CharField(default='', max_length=256, blank=True,
                           verbose_name='又名')
    alt = models.URLField(default='', max_length=256, blank=True,
                          verbose_name='条目页URL')

    # rating
    average = models.DecimalField(default='', max_digits=9, decimal_places=2,
                                  blank=True, verbose_name='评分')
    ratings_count = models.CharField(default='', max_length=20, blank=True,
                                     verbose_name='评分人数')

    # images
    small = models.URLField(default='', max_length=256, blank=True,
                            verbose_name='小封面')
    medium = models.URLField(default='', max_length=256, blank=True,
                             verbose_name='中封面')
    large = models.URLField(default='', max_length=256, blank=True,
                            verbose_name='大封面')

    subtype = models.CharField(default='', max_length=10, blank=True,
                               verbose_name='条目分类')
    directors = models.TextField(default='', blank=True,
                                 verbose_name='导演')
    casts = models.TextField(default='', blank=True,
                             verbose_name='主演')
    year = models.CharField(default='', blank=True, max_length=5,
                            verbose_name='年代')
    languages = models.CharField(default='', blank=True, null=True,
                                 max_length=50, verbose_name='语言')
    genres = models.CharField(default='', blank=True, max_length=128,
                              verbose_name='影片类型')
    countries = models.CharField(default='', blank=True, max_length=128,
                                 verbose_name='制片国家/地区')
    summary = models.TextField(default='', blank=True,
                               verbose_name='简介')