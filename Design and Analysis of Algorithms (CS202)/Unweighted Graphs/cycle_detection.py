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

def DFS(u): # i want to use this to understand if there are any back edges or not
    
    # how are you going to modify DFS to detect cycles?
    # when a cycle is detected, what are the colors of the nodes along the cycle?
    # complete this function to detect cycle.
    global color, parent, cycle_detected
    color[u] = 'GRAY'
    for v in adjlist[u]:
        if color[v] == 'WHITE':
            parent[v] = u
            DFS(v) # activated by other vertices through recursion
        elif color[v] == 'GRAY' and parent[u] != v: # parent of u is not considered as a back edge
            # cycle detected
            cycle_detected = True 

    color[u] = 'BLACK'

num_tree_comp, num_comp_with_cycle = 0, 0
color, parent = {u: 'WHITE' for u in adjlist}, {}
for u in adjlist:
    if color[u] == 'WHITE':
        cycle_detected = False
        DFS(u)
        if cycle_detected:
            num_comp_with_cycle += 1
        else:
            num_tree_comp += 1

print("Number of tree components:", num_tree_comp)
print("Number of components with cycle:", num_comp_with_cycle)