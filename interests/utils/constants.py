# -*- coding: utf-8 -*-
NORMAL_CODE = 0  # 正常状态
INVALID_QUERY_STRING = 101  # 参数错误
REQUEST_ERROR = 102
VALUE_ERROR = 103

success_res = {"msg": "success", "code": NORMAL_CODE, "data": []}
invalid_query_res = {"msg": "Problems parsing query string", "code": INVALID_QUERY_STRING, "data": []}
request_error_res = {"msg": "Request Error", "code": REQUEST_ERROR, "data": []}
value_error_res = {"msg": "value Error", "code": VALUE_ERROR, "data": []}