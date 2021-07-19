#!/usr/bin/env python3

"""
说明：搜索图的测试方法
来源：Programming Python
作者：scarlet
备注：算法按深度优先规则
"""

Graph = {
    'A': ['B', 'E', 'G'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['C', 'F', 'G'],
    'F': [],
    'G': ['A']
}

def tests(searcher):
    print(searcher('E', 'D', Graph)) # 查找 `E`和`D`之间的所有路径
    for x in ['AG', 'GF', 'BA', 'DA']: 
        print(x, searcher(x[0], x[1], Graph))