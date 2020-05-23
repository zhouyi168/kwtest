#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: run.py
@time: 2020/05/23
"""
import unittest
from common import con_path
from HTMLTestRunnerNew import HTMLTestRunner
import time
import os

suite=unittest.TestSuite()
testload=unittest.TestLoader()
discover=unittest.defaultTestLoader.discover(con_path.case_path,pattern='test*.py',top_level_dir=None)
mkfile=time.strptime(time.localtime(),format='%Y-%m-%d %X')
with open('{}.html'.format(os.path.join(con_path.report_path,mkfile)),'wb+') as f:
    runner=HTMLTestRunner(f)
    runner.run(discover)


