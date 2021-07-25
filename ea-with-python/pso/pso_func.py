#!/usr/bin/env python3

"""
说明：PSO的函数写法
来源：MATLAB 智能算法
作者：scarlet
备注：naive PSO
"""
import numpy as np

def PSO(fitness, N, c1, c2, w, M, D):
    """
    c1 学习因子1
    c2 学习因子2
    w 惯性权重
    M 最大迭代次数
    D 搜索空间维数
    N 初始化群体个体数目
    """
    # 初始化种群的个体 
    x = np.random.rand(N, D) #位置
    v = np.random.rand(N, D) #速度

    # pi 代表个体极值
    y = np.copy(x) # 个体最优
    p = np.zeros(N)
    for i, val in enumerate(x):
        p[i] = fitness(val) # 计算适应度

    # pg 全局最优
    pg = x[N-1]
    for i in range(N-1):
        if fitness(x[i]) < fitness(pg):
            pg = x[i]

    # 主要循环
    pbest = np.zeros(M)
    for t in range(M):
        for i in range(N):
            # momentum + cognition + social
            v[i] = w * v[i] + c1 * np.random.random() * (y[i] - x[i])  + c2 * np.random.random() * (pg - x[i])
            x[i] = x[i] + v[i]
            if fitness(x[i]) < p[i]: # 更新个体极值
                p[i] = fitness(x[i]) 
                y[i] = x[i]
            if p[i] < fitness(pg): # 更新全局极值
                pg = y[i]
        pbest[t] = fitness(pg)
    print(f'目标函数取最小值时的自变量 {pg}')
    print(f'目标函数的最小值为 {fitness(pg)}')

def func(x):
    f = lambda x: x**2 + x - 6
    return np.sum(f(x))

if __name__ == '__main__':
    PSO(func, 50, 1.5, 2.5, 0.5, 10000, 30)
    
