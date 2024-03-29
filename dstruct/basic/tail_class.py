#!/usr/bin/env python3

"""
说明：堆栈的类写法
来源：Programming Python
作者：scarlet
备注：列表尾作为栈顶
"""
class error(Exception): pass

class Stack:
    def __init__(self, start=[]) -> None:
        self.stack = []
        for x in start: self.push(x)

    def push(self, obj):
        self.stack.append(obj)
    
    def pop(self):
        if not self.stack: raise error('underflow')
        return self.stack.pop()

    def top(self):
        if not self.stack: raise error('underflow')
        return self.stack[-1]
    
    def empty(self):
        return not self.stack

    def __len__(self):
        return len(self.stack)

    def __getitem__(self, offset):
        return self.stack[offset] # instance[offset] / in / for 
    
    def __repr__(self):
        return f'[Stack: {self.stack}]'
    
    