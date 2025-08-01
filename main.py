from collections import deque


class Graph:
    def breadth_first_search(self, v):
        order = []
        visited = {v}
        to_visite = deque([v])
        while to_visite:
            vertex_name = to_visite.popleft()
            vertex = sorted(self.graph[vertex_name])
            for neighbor in vertex:
                if neighbor not in visited:
                    visited.add(neighbor)
                    to_visite.append(neighbor)
            order.append(vertex_name)
        return order

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
