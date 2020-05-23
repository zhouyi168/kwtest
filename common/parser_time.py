#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: parser_time.py
@time: 2020/04/24
"""

import time
def strftime():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
def strftime_ymd():
    return time.strftime('%Y-%m-%d',time.localtime())
def strftime_hms():
    return time.strftime('%H-%M-%S',time.localtime())