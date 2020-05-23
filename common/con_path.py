#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: con_path.py
@time: 2020/04/24
"""
import os

base_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
data_path=os.path.join(base_path,'data')
testdata_path=os.path.join(data_path,'testdata.xlsx')
pic_path=os.path.join(base_path,'pic')
report_path=os.path.join(base_path,'reports')
case_path=os.path.join(base_path,'testcase')
