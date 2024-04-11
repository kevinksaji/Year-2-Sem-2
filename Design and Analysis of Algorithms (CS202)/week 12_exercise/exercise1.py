import random
import time
import math

################### The following implements the Branch and Bound algorithm for TSP #################
maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif(adj[i][j] <= second and
            adj[i][j] != first):
            second = adj[i][j]

    return second

def TSPRec(graph, curr_bound, curr_weight,
            level, curr_path, visited):
    global final_res
    
    if level == N:
        if graph[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + graph[curr_path[level - 1]]\
                                        [curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (graph[curr_path[level-1]][i] != 0 and
                            visited[i] == False):
            temp = curr_bound
            curr_weight += graph[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= ((firstMin(graph, curr_path[level - 1]) +
                                firstMin(graph, i)) / 2)
            else:
                curr_bound -= ((secondMin(graph, curr_path[level - 1]) +
                                firstMin(graph, i)) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                
                TSPRec(graph, curr_bound, curr_weight,
                    level + 1, curr_path, visited)

            curr_weight -= graph[curr_path[level - 1]][i]
            curr_bound = temp

            # Also reset the visited array
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSPBB(graph):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(graph, i) +
                    secondMin(graph, i))

    curr_bound = math.ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0

    TSPRec(graph, curr_bound, 0, 1, curr_path, visited)
    

################### The following implements the nearest city heursitics for TSP #################
def TSPNearestRec(map, start, tour):
    if len(tour) == len(map): # all cities have been visited
        return

    min_distance = float('inf') # initialize the minimum distance to infinity
    next_city = None # initialize the next city to None

    for i in range(len(map)): # iterate through all cities
        if i not in tour and map[start][i] < min_distance: # if the city has not been visited and the distance to the city is less than the minimum distance
            min_distance = map[start][i] # update the minimum distance
            next_city = i # update the next city

    tour.append(next_city) # add the next city to the tour
    TSPNearestRec(map, next_city, tour) # recursively call the function with the next city as the start city
    
                
def TSPNearest(map, root=0):
    tour = []
    TSPNearestRec(map, root, tour)
    tour.append(0)
    cost = 0
    for i in tour:
        cost += map[tour[i]][tour[i+1]]
    return tour, cost 


# Geneate a graph in the form of an adjacency matrix
def generate_graph(num_vertices):
    # initialize adjacency matrix as a nested list of zeros
    graph = [[0 for j in range(num_vertices)] for i in range(num_vertices)]
    
    # add edges between all pairs of vertices except the last one
    for i in range(num_vertices - 1):
        for j in range(i+1, num_vertices):
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight

    # make sure the first vertex has no incoming edges
    for i in range(1, num_vertices):
        incoming_edges = [graph[j][i] for j in range(num_vertices)]
        if sum(incoming_edges) == 0:
            weight = random.randint(1, 10)
            graph[0][i] = weight
            graph[i][0] = weight
            break

    # make sure the last vertex has no outgoing edges
    for i in range(num_vertices - 2, -1, -1):
        outgoing_edges = graph[i]
        if sum(outgoing_edges) == 0:
            weight = random.randint(1, 10)
            graph[i][num_vertices - 1] = weight
            graph[num_vertices - 1][i] = weight
            break

    return graph

N = 13
graph = generate_graph(N)

final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize

start = time.time()
TSPBB(graph)
print("Branch and Bound: ({}, {}).".format(final_path, final_res))
print('It took %.6f seconds.' % (time.time() - start))
print()
start = time.time()
print("Nearest City Heuristics：{}.".format(TSPNearest(graph)))
print('It took %.6f seconds.' % (time.time() - start))
