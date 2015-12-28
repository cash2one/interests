# -*- coding: utf-8 -*-
from .base import *
from utils.config import Config
import os
import re

MYSQL_CONFIG = Config.get('config', 'mysql')

db_host = MYSQL_CONFIG.get('default').get('host')
db_port = MYSQL_CONFIG.get('default').get('port')
db_name = MYSQL_CONFIG.get('default').get('db')
db_user = MYSQL_CONFIG.get('default').get('user')
db_password = MYSQL_CONFIG.get('default').get('password')

pattern = re.compile('^%.*%$')

if pattern.match(str(db_host)):
    db_host = os.environ.get(db_host.strip('%'), None)

if pattern.match(str(db_port)):
    db_port = os.environ.get(db_port.strip('%'), None)

if pattern.match(str(db_name)):
    db_name = os.environ.get(db_name.strip('%'), None)

if pattern.match(str(db_user)):
    db_user = os.environ.get(db_user.strip('%'), None)

if pattern.match(str(db_password)):
    db_password = os.environ.get(db_password.strip('%'), None)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
    },
    # 'online_goods_service': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': MYSQL_CONFIG.get('online_goods_service').get('host'),
    #     'PORT': MYSQL_CONFIG.get('online_goods_service').get('port'),
    #     'NAME': MYSQL_CONFIG.get('online_goods_service').get('db'),
    #     'USER': MYSQL_CONFIG.get('online_goods_service').get('user'),
    #     'PASSWORD': MYSQL_CONFIG.get('online_goods_service').get('password'),
    #     'OPTIONS': {
    #         'init_command': 'SET storage_engine=INNODB',
    #     }
    # }
}

