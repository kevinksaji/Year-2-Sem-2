digraph = [('a', 'b'), ('b', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
           ('c', 'g'), ('d', 'c'), ('d', 'h'), ('e', 'a'), ('e', 'f'),
           ('f', 'g'), ('g', 'f'), ('g', 'h'), ('h', 'h')]

vertex = []
adj = [{}, {}]
for u, v in digraph:
    if u not in vertex:
        vertex.append(u)
    if v not in vertex:
        vertex.append(v)
    if u not in adj[0]:
        adj[0][u] = []
    if v not in adj[1]:
        adj[1][v] = []
    adj[0][u].append(v)
    adj[1][v].append(u)

def kosaraju(u, revers):
    global visited, stack
    if visited[u]:
        return
    visited[u] = True
    neigh = adj[revers][u]
    for v in neigh:
        kosaraju(v, revers)
    stack.append(u)

stack = []
visited = {u: False for u in vertex}
for u in vertex:
    kosaraju(u, 0)
num_scc = 0
visited = {u: False for u in vertex}
for u in stack[::-1]:
    if not visited[u]:
        num_scc += 1
        kosaraju(u, 1)

print('number of strongly connected components:', num_scc)
