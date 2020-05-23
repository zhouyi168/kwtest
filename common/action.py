#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: action.py
@time: 2020/04/14
"""
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
import time
from common.getelement import GetElement
from common import parser_time
from common import con_path
from common.create_dir import *

class Action:
    def __init__(self):
        self.driver=None


    def openbrowse(self,browse):
        if browse=='ie':
            self.driver=webdriver.Ie()
        elif browse=='chrom':
            self.driver=webdriver.Chrome()
        elif browse=='firefox':
            self.driver=webdriver.Firefox()
        # pic_name=self.capture_screen()
        # return pic_name

    def visiturl(self,url):
        try:
            self.driver.get(url)
        except TimeoutException as e:
            print('访问url:{} 超时'.format(url))
        # pic_name=self.capture_screen()
        # return pic_name


    def pause(self,second):
        time.sleep(float(second))
        # pic_name = self.capture_screen()
        # return pic_name

    def click(self,locator_type,expresstion):
        GetElement(self.driver).getelement(locator_type,expresstion).click()
        # pic_name = self.capture_screen()
        # return pic_name

    def input(self,locator_type,expresstion,value):
        GetElement(self.driver).getelement(locator_type, expresstion).clear()
        GetElement(self.driver).getelement(locator_type, expresstion).send_keys(value)
        # pic_name = self.capture_screen()
        # return pic_name

    def enter_frame(self,locator_type,expresstion,value):
        self.driver.switch_to.frame(GetElement(self.driver).getelement(locator_type, expresstion))
        # pic_name = self.capture_screen()
        # return pic_name

    def assert_word(self,value):
        try:
            assert value in self.driver.page_source

            print('断言成功')
            return True
        except AssertionError as e:
            print('断言失败')
            return False
        # pic_name = self.capture_screen()
        # return pic_name

    def capture_screen(self):
        try:
            path=create_dir(con_path.pic_path)
            file_path=os.path.join(path,parser_time.strftime_hms()+'.png')
            print(file_path)
            self.driver.save_screenshot(file_path)
            return file_path
        except Exception as e:
            print('截图出错')
            raise e


    def close_browser(self):
        self.driver.close()


    def quit(self):
        self.driver.quit()


if __name__=="__main__":
    action=Action()
    action.openbrowse('chrom')
    action.visiturl('https://www.baidu.com/')
    action.input(By.ID,'kw','python学习课程')
    action.click(By.ID,'su')
    action.pause(2)
    action.quit()










