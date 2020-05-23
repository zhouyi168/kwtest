#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: command.py
@time: 2020/04/24
"""
from common.action import Action

# class FunctionCommand:
#     # def __init__(self,act):
#     #     self.act = act
#     @staticmethod
#     def no_args(action):
#         command='Action().%s()'%(action)
#         return command
#
#     @staticmethod
#     def no_value(action,local_type,expresstion):
#         command='Action().%s("%s","%s")'%(action,local_type,expresstion)
#         return command
#
#     @staticmethod
#     def all_args(action,local_type,expresstion,value):
#         command='Action().%s("%s","%s","%s")'%(action,local_type,expresstion,value)
#         return command
#
#     @staticmethod
#     def no_local_express(action,value):
#         command = 'Action().%s("%s")' % (action, value)
#         return command

def chcomm(action,local_type,expresstion,value):
    if local_type is None and expresstion is None and value is None:
        command='act.%s()'%(action)
    elif local_type is None and expresstion is None:
        command = 'act.%s("%s")' % (action, value)
    elif value is None:
        command = 'act.%s("%s","%s")' % (action, local_type, expresstion)
    else:
        command = 'act.%s("%s","%s","%s")' % (action, local_type, expresstion, value)
    return command


if __name__=="__main__":
    from common.action import Action
    act=Action()
    command=chcomm(action='openbrowse',value='chrom')
    print(command)
    t=eval(command)
    print(t)


