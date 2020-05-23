#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: create_dir.py
@time: 2020/04/24
"""
import os
from common import con_path
from common import parser_time

def create_dir(path):
    path=os.path.join(path,parser_time.strftime_ymd())
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return path
