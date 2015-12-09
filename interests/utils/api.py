# -*- coding: utf-8 -*-
import traceback

import requests
from requests import codes
from utils.log import logger


class APIError(Exception):

    def __init__(self, code=None, message=None):
        self.code = code
        self.message = message

    def __str__(self):
        return 'code={}, message={}'.format(self.code, self.message)


class APIClient(object):

    def __init__(self, api_baseurl=None, timeout=8):
        self.api_baseurl = api_baseurl
        self.timeout = timeout

    def build_url(self, path, qs=''):
        url = '{}{}'.format(self.api_baseurl, path)
        if qs:
            url += '?' + qs
        return url

    @staticmethod
    def request(method, url, data=None, json=None, timeout=None):
        logger.info('APIClient request: {0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}'.format(method, url, data, json, timeout))
        try:
            response = requests.request(method, url, data=data, json=json,
                                        timeout=timeout)
        except requests.exceptions.RequestException:
            raise APIError(code=-1, message=traceback.format_exc())
        if response.status_code == codes.OK:
            try:
                response_dict = response.json()
            except ValueError as e:
                raise APIError(code=-1,
                               message=('response content: {}\n'
                                        'error: {}'.format(
                                            response.content, e)))
            if response_dict['code'] != 0:
                raise APIError(code=response_dict['code'],
                               message=response_dict.get('msg'))
        else:
            raise APIError(code=response.status_code,
                           message=response.content)

        return response
