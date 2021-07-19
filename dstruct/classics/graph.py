"""
说明：图对象
来源：Programming Python
作者：scarlet
备注：
"""


class Graph:
    def __init__(self, label, extra=None) -> None:
        self.name = label # 节点是类实例
        self.data = extra # 图由类实例链接而成
        self.arcs = []
    
    def __repr__(self):
        return self.name

    def search(self, goal):
        Graph.solns = []
        self.generate([self], goal)
        Graph.solns.sort(key=lambda x: len(x))
        return Graph.solns
    
    def generate(self, path, goal):
        if self == goal:
            Graph.solns.append(path)
        else:
            for arc in self.arcs:
                if arc not in path:
                    arc.generate(path + [arc], goal)