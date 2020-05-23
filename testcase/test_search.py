#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: test_search.py
@time: 2020/04/14
"""

import unittest
from common import con_path
from common.action import Action
from common.do_excel import DoExcel
from common.command import *
from ddt import data,ddt

datas=DoExcel(con_path.testdata_path).readexcel('baidu')
act=Action()
@ddt
class Search(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     openbrowse_data=DoExcel(con_path.testdata_path).readrow('baidu',1)
    #     try:
    #         eval(FunctionCommand.no_local_express(openbrowse_data.action,openbrowse_data.value))
    #         DoExcel(con_path.testdata_path).write_excel('baidu',2,8,'Pass')
    #     except Exception as e:
    #         print('打开浏览器失败')
    #         DoExcel(con_path.testdata_path).write_excel('baidu', 2, 8, 'Faild')
    @data(*datas)
    def test_search(self,case):
        command=chcomm(case.action,case.locate_type,case.expression,case.value)
        print(command)
        try:
            eval(command)
            print('{}执行成功'.format(case.title))
            DoExcel(con_path.testdata_path).write_excel('baidu',int(case.id)+1,8,'Pass')
        except Exception as e :
            pic=act.capture_screen()
            print('{}执行失败'.format(case.title))
            DoExcel(con_path.testdata_path).write_excel('baidu', int(case.id)+1, 8, 'Failed')
            DoExcel(con_path.testdata_path).write_excel('baidu', int(case.id)+1, 9, e)
            DoExcel(con_path.testdata_path).write_excel('baidu', int(case.id)+1, 10, pic)

