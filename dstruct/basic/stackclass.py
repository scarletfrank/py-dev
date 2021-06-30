#!/usr/bin/env python3

"""
说明：堆栈的类写法
来源：Programming Python
作者：scarlet
备注：列表头作为栈顶
"""

class error(Exception): pass

class Stack:
    def __init__(self, start=[]) -> None:
        self.stack = []
        for x in start: self.push(x)
        self.reverse()              # 入栈之后再反序，？
    
    def push(self, obj):
        self.stack = [obj] + self.stack # 列表头作为栈顶    

    def pop(self):
        if not self.stack: raise error('underflow')
        top, *self.stack = self.stack
        return top
    
    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[0]
    
    def empty(self):
        return not self.stack
    
    # 重载
    def __repr__(self) -> str:
        # print(instance)
        return f'[Stack:{self.stack}]'
    
    def __eq__(self, o: object) -> bool:
        # == !=
        return self.stack == o.stack
    
    def __len__(self):
        # len(instance)
        return len(self.stack)
    
    def __add__(self, other):
        # instance + instance
        return Stack(self.stack + other.stack)
    
    def __mul__(self, reps):
        # instance * reps
        return Stack(self.stack * reps) # instance * reps
    
    def __getitem__(self, offset):
        # instance[i]
        return self.stack[offset]

    def __getattr__(self, name):
        # instance.reverse()
        return getattr(self.stack, name)
