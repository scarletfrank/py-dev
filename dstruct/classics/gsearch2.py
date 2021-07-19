"""
说明：用路径栈代替递归实现图搜索
来源：Programming Python
作者：scarlet
备注：
"""

def search(start, goal, graph):
    solns = generate(([start], []), goal, graph)
    solns.sort(key=lambda x : len(x))
    return solns

def generate(paths, goal, graph):
    solns = []
    while paths:
        front, paths = paths # 弹出栈顶的路径
        state = front[-1]
        if state == goal:
            solns.append(front)
        else:
            for arc in graph[state]:
                if arc not in front:
                    paths = (front + [arc]), paths
    return solns

if __name__ == '__main__':
    import gtestfunc
    gtestfunc.tests(search)