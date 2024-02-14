import random

random.seed('connected')

n = 1000
m = 2000
adjlist = {i:[] for i in range(n)}
for _ in range(2000):
    while True:
        i, j = random.randrange(n), random.randrange(n)
        if i != j:
            adjlist[i].append(j)
            adjlist[j].append(i)
            break

def DFS(u):
    global color, parent
    color[u] = 'GRAY'
    for v in adjlist[u]:
        if color[v] == 'WHITE':
            parent[v] = u
            DFS(v)
    color[u] = 'BLACK'

# very simple modification
# you do not need to change the DFS function itself

color, parent = {u: 'WHITE' for u in adjlist}, {}
num_components = 0
for u in adjlist:
    if color[u] == 'WHITE':
        num_components += 1
        DFS(u)
print("there are %d components" % num_components)