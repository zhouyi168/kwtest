#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: getelement.py
@time: 2020/04/23
"""
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
class GetElement:
    def __init__(self,driver):
        self.driver=driver

    def getelement(self,locator_type,expresstion):
        try:
            ele=WebDriverWait(self.driver,20).until(lambda x:x.find_element(locator_type,expresstion))
            return ele

        except TimeoutException as e:
            print('获取元素超时')

    def getelements(self,locator_type,expresstion):
        try:
            eles=WebDriverWait(self.driver,20).until(lambda x:x.find_elements(locator_type,expresstion))
            return eles

        except TimeoutException as e:
            print('获取元素超时')