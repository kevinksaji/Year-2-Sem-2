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
    global color, parent, cycle_detected # you need to declare these variables as global. the color variable is a dictionary that stores the color of each vertex, and the parent variable is a dictionary that stores the parent of each vertex
    color[u] = 'GRAY' # set the color of the vertex to GRAY because we are visiting it and it is now discovered
    for v in adjlist[u]: # for each vertex v that is adjacent to u
        if color[v] == 'WHITE': # if the color of v is WHITE, then v has not been visited yet
            parent[v] = u # set the parent of v to u
            DFS(v) # recursively visit v
        elif color[v] == 'GRAY' and parent[u] != v: # if the color of v is GRAY and v is not the parent of u, then a cycle is detected
            cycle_detected = True
    color[u] = 'BLACK'

# very simple modification
# you do not need to change the DFS function itself

color, parent = {u: 'WHITE' for u in adjlist}, {} # initialize the color of each vertex to WHITE and the parent of each vertex to None
num_components, num_cycle = 0, 0 # initialize the number of components to 0, this variable will store the number of connected components in the graph
for u in adjlist:
    if color[u] == 'WHITE': # if the color of the vertex is WHITE, then the vertex has not been visited yet
        cycle_detected = False
        DFS(u)
        if cycle_detected:
            num_cycle += 1
        else:
            num_components += 1
print("there are %d cycles" % num_cycle)
print("there are %d components" % num_components)

# The above algorithm works because the DFS function visits all the vertices in a connected component starting from a vertex u. If there are any vertices that are not visited, then the DFS function is called again with that vertex as the starting vertex. This process continues until all the vertices are visited. 
# The number of times the DFS function is called is equal to the number of connected components in the graph.