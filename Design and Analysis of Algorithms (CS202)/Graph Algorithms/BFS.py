n = 12
m = 18
adjlist = {i:[] for i in range(n)}
for i in range(6):
    adjlist[i].extend(((i+1)%6, (i+5)%6))
    adjlist[i].append(i+6)
for i in range(6, 12):
    adjlist[i].append(i-6)
    adjlist[i].extend((6+(i+2)%6, 6+(i+4)%6))

def BFS(s):
    global color, parent, depth
    color[s], depth[s] = 'GRAY', 0
    queue = [s]
    while queue:
        u = queue.pop(0)
        print(u, 'dequeued, the queue is now:', queue)
        for v in adjlist[u]:
            if color[v] == 'WHITE':
                color[v] = 'GRAY'
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
        color[u] = 'BLACK'
        print('after exploring', u, ', the queue is now:', queue)

color, parent, depth = {u: 'WHITE' for u in adjlist}, {}, {}
for u in adjlist:
    if color[u] == 'WHITE':
        BFS(u)
