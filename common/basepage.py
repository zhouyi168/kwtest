#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: basepage.py
@time: 2020/04/25
"""
from common import con_path
from common.action import Action
from common.do_excel import DoExcel
from common.command import FunctionCommand
import time

class BasePage:
    @staticmethod
    def openbrowse():
        openbrowse_data = DoExcel(con_path.testdata_path).readrow('baidu', 1)
        try:
            start_time=time.time()
            pic_name=eval(FunctionCommand().no_local_express(openbrowse_data.action, openbrowse_data.value))
            end_time=time.time()
            exec_time='%s.2f'%(end_time-start_time)
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 8, '成功')
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 7, exec_time)
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 10, pic_name)
        except Exception as e:
            pic_name=Action().capture_screen()
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 8, '失败')
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 9, e)
            DoExcel(con_path.testdata_path).write_excel('baidu', 2, 10, pic_name)

if __name__=="__main__":
    BasePage.openbrowse()


