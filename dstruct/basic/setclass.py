#!/usr/bin/env python3

"""
说明：集合的类写法
来源：Programming Python
作者：scarlet
备注：列表
"""

class Set:
    def __init__(self, value = []) -> None:
        self.data = []
        self.concat(value)
    
    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)
    
    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)
    
    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self) -> str: return f'<Set: {repr(self.data)}>'