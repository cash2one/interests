# -*- coding: utf-8 -*-
import os
# from celery.schedules import crontab
import djcelery
from utils.config import Config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


PROJECT_DIR = os.path.dirname(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+#gzk#wixbq91s@#e8rz2m6qc)-=d3_i*l=6(a(6bi^%&$!alb'

MAIN_CONFIG = Config.get('config', 'main')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = MAIN_CONFIG.get('debug', True)

TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ['*']

COMMON_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'rest_framework',
]

PROJECT_APPS = [
    'apps.books',
    'apps.fit',
    'apps.music',
    'apps.movies',
    'apps.profile',
    'apps.programskills',
]

INSTALLED_APPS = COMMON_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'etc/db.sqlite3'),
    },
}

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "static"),
#)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'static/templates'),
)

# Django Log
DJANGO_LOG_DIR = os.path.join(PROJECT_DIR, MAIN_CONFIG.get('log_dir'))

if not os.path.exists(DJANGO_LOG_DIR):
    os.makedirs(DJANGO_LOG_DIR)

LOG_NAME = os.path.join(DJANGO_LOG_DIR, MAIN_CONFIG.get('log_file'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': (' %(levelname)s: [%(asctime)s][%(pathname)s:%(lineno)d]'
                       ':\n %(message)s\n')
        },
    },
    'handlers': {
        'file': {
            'when': 'D',
            'level': 'INFO',
            'filename': LOG_NAME,
            'formatter': 'verbose',
            'class': 'logging.handlers.TimedRotatingFileHandler',
        },
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'propagate': True,
            'handlers': ['file'],
        },
    },
}

# cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

djcelery.setup_loader()
# CELERYBEAT_SCHEDULE = {
#     'update_stock_data': {
#         'task': 'utils.import_real_stock.import_real_stock',
#         'schedule': crontab(hour='*'),
#         'args': (),
#     },
# }

BROKER_URL = Config.get('config').get('rabbitmq')
# CELERY_IMPORTS = ("utils.sync_stock", )

# services api baseurl
API_URL = Config.get('config').get('ofc_warehouse_url')
