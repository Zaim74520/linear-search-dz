from collections import deque


class DirectedGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)

    def __repr__(self):
        return str(self.adj)


def bfs(graph: DirectedGraph, start):
    if start not in graph.adj:
        return []

    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor in graph.adj.get(v, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def build_adjacency_matrix(edges):
    vertices = []
    seen = set()
    for u, v in edges:
        if u not in seen:
            seen.add(u)
            vertices.append(u)
        if v not in seen:
            seen.add(v)
            vertices.append(v)

    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        i, j = index[u], index[v]
        matrix[i][j] = 1

    return matrix, vertices


def add_vertex_to_matrix(matrix, vertices, new_vertex):
    if new_vertex in vertices:
        return matrix, vertices

    n = len(matrix)
    for row in matrix:
        row.append(0)
    matrix.append([0] * (n + 1))
    vertices.append(new_vertex)
    return matrix, vertices


def add_edge_to_matrix(matrix, vertices, u, v, weight=1):
    if u not in vertices or v not in vertices:
        raise ValueError("Вершина не найдена")
    i, j = vertices.index(u), vertices.index(v)
    matrix[i][j] = weight


def build_adjacency_list(edges):
    adj = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
    return adj


def add_vertex_to_adj_list(adj, v):
    if v not in adj:
        adj[v] = []


def add_edge_to_adj_list(adj, u, v):
    add_vertex_to_adj_list(adj, u)
    add_vertex_to_adj_list(adj, v)
    if v not in adj[u]:
        adj[u].append(v)


if __name__ == "__main__":
    # 01
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    print("Граф (01):", g)

    # 02
    print("BFS из A (02):", bfs(g, "A"))

    # 03
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    mat, verts = build_adjacency_matrix(edges)
    print("Вершины (матрица) (03):", verts)
    print("Матрица (03):")
    for r in mat:
        print(r)

    mat, verts = add_vertex_to_matrix(mat, verts, "E")
    add_edge_to_matrix(mat, verts, "D", "E", weight=1)
    print("Матрица после добавления E и D->E (03):")
    print("Вершины:", verts)
    for r in mat:
        print(r)

    # 04
    adj_from_edges = build_adjacency_list(edges)
    print("Список смежности из рёбер (04):", adj_from_edges)

    add_vertex_to_adj_list(adj_from_edges, "E")
    add_edge_to_adj_list(adj_from_edges, "D", "E")
    print("Список смежности после изменений (04):", adj_from_edges)
