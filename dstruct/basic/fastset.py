#!/usr/bin/env python3

"""
说明：集合的类写法
来源：Programming Python
作者：scarlet
备注：使用字典将集合性能优化成线性的
"""

class Set:
    def __init__(self, value) -> None:
        self.data = {}
        self.concat(value)
    
    def intersect(self, other):
        res = {}
        for x in other:
            if x in self.data:
                res[x] = None
        return Set(res.keys())
    
    def union(self, other):
        res = {}
        for x in other:
            res[x] = None
        for x in self.data.keys():
            res[x] = None
        return Set(res.keys())
    
    def concat(self, value):
        for x in value: self.data[x] = None
    
    def __getitem__(self, key):
        return list(self.data.keys())[key]
    
    def __repr__(self) -> str:
        return f'<Set:{list(self.data.keys())}>'
    
    def __len__(self): return len(self.data)
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
