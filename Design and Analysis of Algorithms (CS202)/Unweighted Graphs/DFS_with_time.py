n = 12
m = 18
adjlist = {i:[] for i in range(n)}
for i in range(6):
    adjlist[i].extend(((i+1)%6, (i+5)%6))
    adjlist[i].append(i+6)
for i in range(6, 12):
    adjlist[i].append(i-6)
    adjlist[i].extend((6+(i+2)%6, 6+(i+4)%6))

def DFS(u):
    global color, parent, start, end, time
    # modify the original DFS algorithm
    # to record the start and end time of exploring node u

color, parent, start, end = {u: 'WHITE' for u in adjlist}, {}, {}, {}
time = 0
for u in adjlist:
    if color[u] == 'WHITE':
        DFS(u)

for u in adjlist:
    print(u, 'started at', start[u], 'completed at', end[u])
