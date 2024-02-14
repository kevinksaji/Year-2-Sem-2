n = 12
m = 18
#building a graph that is represented using adjacent lists
adjlist = {i:[] for i in range(n)}
for i in range(6):
    adjlist[i].extend(((i+1)%6, (i+5)%6))
    adjlist[i].append(i+6)
for i in range(6, 12):
    adjlist[i].append(i-6)
    adjlist[i].extend((6+(i+2)%6, 6+(i+4)%6))

def DFS(u, level):
    global color, parent
    color[u] = 'GRAY'
    print('  ' * level, '-- start exploring', u)
    for v in adjlist[u]:
        if color[v] == 'WHITE':
            parent[v] = u
            DFS(v, level + 1)
        elif color[v] == 'GRAY':
            print('  ' * level, v, ' is being explored')
        elif color[v] == 'BLACK':
            print('  ' * level, v, ' is done with exploration')
    color[u] = 'BLACK'
    print('  ' * level, '-- end exploring', u)

color, parent = {u: 'WHITE' for u in adjlist}, {}
for u in adjlist:
    if color[u] == 'WHITE':
        DFS(u, 0)
