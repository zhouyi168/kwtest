#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: test.py
@time: 2020/05/04
"""


# def feibo(n):
#     if n<=1:
#         return n
#     elif n<=2:
#         return 1
#     return feibo(n-1)+feibo(n-2)
#
# n=int(input('请输入一个数字'))
# feibo_list=[]
# i=0
# while i<=n:
#     feibo_list.append(feibo(i))
#     i+=1
# print(feibo_list)

def outer(func):
    def inner(*args,**kwargs):
        c=func(*args,**kwargs)
        print(c)
    return inner
@outer
def func1(a,b=1):
    return a*b

func1(5,5)



