import heapq
from typing import List, Tuple
import random

def generate_graph(n: int):
    """
    Generates a graph in the form of an adjacency matrix with n vertices.
    :param n: The number of vertices in the graph.
    :return: The adjacency matrix of the graph.
    """
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[i][j] = graph[j][i] = random.randint(1, 10)
    return graph

def prim_tsp(graph: List[List[int]]):
    """
    Returns an approximation of the TSP using Prim's algorithm.
    where parameter graph is an adjacency matrix of the graph.
    TODO: update the following code to output the travelling cost
    """
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    heap = [(weight, 0, i) for i, weight in enumerate(graph[0])]
    heapq.heapify(heap)
    cycle = [0]
    while len(cycle) < n:
        weight, u, v = heapq.heappop(heap)
        if not visited[v]:
            visited[v] = True
            cycle.append(v)
            for w, weight in enumerate(graph[v]):
                if not visited[w]:
                    heapq.heappush(heap, (weight, v, w))
    cycle.append(0)
    return cycle

random.seed(42)
print(prim_tsp(generate_graph(4)))