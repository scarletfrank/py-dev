#!/usr/bin/env python3

"""
说明：实现内置类型的子类
来源：Programming Python
作者：scarlet
备注：列表
"""

class Stack(list):
    def top(self):
        return self[-1]
    
    def push(self, item):
        list.append(self, item)
    
    def pop(self):
        if not self:
            return None
        else:
            return list.pop(self)
    
class Set(list):
    def __init__(self, value=[]):
        list.__init__(self)
        self.concat(value)
    
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)
    
    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res
    
    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)
    
    # 继承len getitem和iter方法，用列表repr
    def __add__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __str__(self): return f'<Set: {repr(self)}>'
