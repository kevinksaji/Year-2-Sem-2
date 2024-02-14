'''
graph = {'m': ['q', 'r', 'x'],
           'n': ['o', 'q', 'u'],
           'o': ['r', 's', 'v'],
           'p': ['o', 's', 'z'],
           'q': ['t'],
           'r': ['u', 'y'],
           's': ['r'],
           't': [],
           'u': ['t'],
           'v': ['w', 'x'],
           'w': ['z'],
           'x': [],
           'y': ['v'],
           'z': []}
'''

graph = {
    '1': ['2'],
    '2': ['3'],
    '3': []
}

def DFS_with_tsort(u):
    global color, parent, start, end, time
    color[u] = 'GRAY'
    time += 1
    start[u] = time
    for v in graph[u]:
        if color[v] == 'WHITE':
            parent[v] = u
            DFS_with_tsort(v)
    color[u] = 'BLACK'
    time += 1
    end[u] = time

color, parent, start, end = {u: 'WHITE' for u in graph}, {}, {}, {}
time = 0
for u in graph:
    if color[u] == 'WHITE':
        DFS_with_tsort(u)
for u in graph:
    print(u, 'started at', start[u], 'completed at', end[u])
