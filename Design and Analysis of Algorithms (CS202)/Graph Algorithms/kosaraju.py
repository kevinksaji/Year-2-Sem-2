digraph = [('a', 'b'), ('b', 'c'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
           ('c', 'g'), ('d', 'c'), ('d', 'h'), ('e', 'a'), ('e', 'f'),
           ('f', 'g'), ('g', 'f'), ('g', 'h'), ('h', 'h')]

vertex = [] # list of vertices
adj = [{}, {}] # adjacency list for the original graph and the reversed graph
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

def kosaraju(u, revers): # revers = 0 for the original graph, revers = 1 for the reversed graph.
    # Declare visited and stack as global variables
    global visited, stack
    if visited[u]:  # Check if the vertex has already been visited
        return
    visited[u] = True  # Mark the vertex as visited
    neigh = adj[revers][u]  # Get the neighbors of the vertex based on the direction
    for v in neigh:  # Iterate through the neighbors
        kosaraju(v, revers)  # Recursively call kosaraju on each neighbor
    stack.append(u)  # Add the vertex to the stack after visiting all its neighbors

stack = []
visited = {u: False for u in vertex}
for u in vertex:
    kosaraju(u, 0)
num_scc = 0
visited = {u: False for u in vertex}
for u in stack[::-1]: # Iterate through the vertices in the reverse order of the stack. so start with the vertex at the top of the stack with the highest finishing time
    if not visited[u]: 
        num_scc += 1
        kosaraju(u, 1)

print('number of strongly connected components:', num_scc)
