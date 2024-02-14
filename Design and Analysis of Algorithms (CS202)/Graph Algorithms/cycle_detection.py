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
    # how are you going to modify DFS to detect cycles?
    # when a cycle is detected, what are the colors of the nodes along the cycle?
    # TODO: complete this function to detect cycle.

color, parent = {u: 'WHITE' for u in adjlist}, {}
for u in adjlist:
    if color[u] == 'WHITE':
        DFS(u)
