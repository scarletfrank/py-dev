#!/usr/bin/env python3

"""
说明：堆栈的元组写法
来源：Programming Python
作者：scarlet
备注：（1, (2, (3, (4, None))))
"""

class Stack:
    def __init__(self, start=[]) -> None:
        self.stack = None
        for i in range(-len(start), 0):
            self.push(start[-i - 1])    # 反序存入栈
    
    def push(self, node): # 根向左上方生长
        self.stack = node, self.stack # 新建的元组 (node, tree)
        return node
    
    def pop(self):
        node, self.stack = self.stack
        return node
    
    def empty(self):
        return not self.stack
    
    def __len__(self):
        len, tree = 0, self.stack
        while tree:
            len, tree = len + 1, tree[1]
        return len
    
    def __getitem__(self, index):
        len, tree = 0, self.stack
        while len < index and tree:
            len, tree = len + 1, tree[1]
        if tree:
            return tree[0]
        else:
            raise IndexError()
        
    def __repr__(self):
        return f'[FastStack: {repr(self.stack)}]'

        
