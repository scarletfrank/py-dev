"""
说明：堆栈的模块写法
来源：Programming Python
作者：scarlet
"""

stack = []
class error(Exception):
    pass

def push(obj):
    global stack
    stack = [obj] + stack