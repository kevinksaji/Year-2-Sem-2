import math
import random

'''
Function to generate the initial solution using the nearest city heuristics
'''
def TSPNearest(map, start, tour):
    tour.append(start)
    nearestDistance = float('inf')
    nearestCity = -1
    for i in range(len(map)):
        if not(i in tour) and map[start][i] < nearestDistance:
            nearestCity = i
            nearestDistance = map[start][i]

    if nearestCity == -1:
        return
    else:
        TSPNearest(map, nearestCity, tour)

'''
Function to implement twice 2-opt neighbourhood search 
'''
def twoPairsExchange(tour):
    bestNeighbour = tour
    bestNeighbourCost = getCost(tour)

    #TODO: implement a neighbourhood search strategy which exchanes 2 pairs of cities 
    # and see whether the tour is improved.
    for i in range(0, len(tour)):
        for j in range(0, len(tour)):
            for k in range(0, len(tour)):
                for l in range(0, len(tour)):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        newtour = tour.copy()
                        newtour[i] = tour[k]
                        newtour[k] = tour[i]
                        newtour[j] = tour[l]
                        newtour[l] = tour[j]
                        newCost = getCost(newtour)
                        if newCost < bestNeighbourCost:
                            bestNeighbourCost = newCost
                            bestNeighbour = newtour

    return bestNeighbour, bestNeighbourCost

'''
Function to implement 2-opt neighbourhood search 
'''
def twoOpt(tour):
    best_2opt_tour, best_2opt_tour_cost = tour, getCost(tour)
    for i in range(0, len(tour)):
        for j in range(0, len(tour)):
            if i != j: # choose the i-th edge (i-th vertex to (i+1)-th vertex) and j-th edge (j-th vertex to (j+1)-th vertex) to swap
                tr = tour.copy()
                tr[i+1:j+1] = reversed(tr[i+1:j+1]) # the entire segment from (i+1)-th vertex to j-th vertex need to be reversed
                tr_cost = getCost(tr)
                if tr_cost < best_2opt_tour_cost:
                    best_2opt_tour, best_2opt_tour_cost = tr, tr_cost
                    return best_2opt_tour, best_2opt_tour_cost
    return best_2opt_tour, best_2opt_tour_cost

'''
Function to implement 3-opt neighbourhood search 
'''
def threeOpt(tour):
    """Iterative improvement based on 3 exchange."""
    tour_cost = getCost(tour)
    best_3opt_tour, best_3opt_tour_cost = tour, tour_cost
    all_3_sep_seg = list(three_separate_segments(len(tour)))
    for (i, j, k) in all_3_sep_seg:
        # Given tour [...A-B...C-D...E-F...]
        A, B, C, D, E, F = tour[i], tour[i+1], tour[j], tour[j+1], tour[k], tour[(k+1) % len(tour)] # k is the last segment, so k+1 could be equal n, when it is n, we retrieve the first vertex
        d = [0] * 8
        d[0] = map[A][B] + map[C][D] + map[E][F] # destroyed segments
        ### the encoding will be explained later ###
        d[2] = map[A][B] + map[C][E] + map[D][F] # a 2-opt with A-B restored and D...E reversed, a better tour if d1 < d0
        d[4] = map[C][D] + map[E][A] + map[F][B] # a 2-opt with C-D restored and F...A reversed, a better tour if d2 < d0
        d[1] = map[E][F] + map[A][C] + map[B][D] # a 2-opt with E-F restored and B...C reversed, a better tour if d3 < d0
        d[3] = map[A][C] + map[B][E] + map[D][F] # a 3-opt with both B...C and D...E reversed, a better tour if d4 < d0
        d[6] = map[C][E] + map[D][A] + map[F][B] # a 3-opt with both D...E and F...A reversed, a better tour if d5 < d0
        d[5] = map[E][A] + map[F][C] + map[B][D] # a 3-opt with both F...A and B...C reversed, a better tour if d6 < d0
        d[7] = map[A][D] + map[E][B] + map[C][F] # the only 3-opt with no reversion but the sequence of the F...A, B...C, and D...E are swapped
        min_d, min_i = d[0], 0
        for ii in range(1, 8):
            if d[ii] < min_d:
                min_d, min_i = d[i], ii
        if min_i == 0:
            continue
        tr = tour.copy()
        # all code should be interpreted in binary representation
        # rightmost bit: reverse B...C
        # middle bit: reverse D...E
        # leftmost bit: reverse F...A
        rbit = min_i % 2
        mbit = min_i // 2 % 2
        lbit = min_i // 4
        if rbit:
            tr[i+1:j+1] = reversed(tr[i+1:j+1])
        if mbit:
            tr[j+1:k+1] = reversed(tr[j+1:k+1])
        if lbit:
            tr[i+1:k+1] = reversed(tr[i+1:k+1])
        '''
        # if we do not use bit representation, the code is equivalent to the block below:
        if min_i == 2:
            tr[j+1:k+1] = reversed(tr[j+1:k+1]) # reverse D...E
        elif min_i == 4:
            tr[i+1:k+1] = reversed(tr[i+1:k+1]) # reverse B...E, in fact should reverse F...A, but this range includes index -1 and index 0
        elif min_i == 1:
            tr[i+1:j+1] = reversed(tr[i+1:j+1]) # reverse B...C
        elif min_i == 3:
            tr[i+1:j+1] = reversed(tr[i+1:j+1])
            tr[j+1:k+1] = reversed(tr[j+1:k+1]) # reverse both B...C and D...E
        elif min_i == 6:
            tr[j+1:k+1] = reversed(tr[j+1:k+1]) # reverse D...E first
            tr[i+1:k+1] = reversed(tr[i+1:k+1]) # then reverse B...D (D: originally the position of E)
        elif min_i == 5:
            tr[i+1:j+1] = reversed(tr[i+1:j+1]) # reverse B...C first
            tr[i+1:k+1] = reversed(tr[i+1:k+1]) # then reverse C...E (C: originally the position of B)
        elif min_i == 7:
            tr[i+1:j+1] = reversed(tr[i+1:j+1]) # reverse B...C first
            tr[j+1:k+1] = reversed(tr[j+1:k+1]) # reverse D...E second
            tr[i+1:k+1] = reversed(tr[i+1:k+1]) # reverse C...D last (C: originally the position of B and D: originally the position of F)'''
        tr_cost = getCost(tr)
        if tr_cost < best_3opt_tour_cost:
            best_3opt_tour, best_3opt_tour_cost = tr, tr_cost
            return best_3opt_tour, best_3opt_tour_cost
    return best_3opt_tour, best_3opt_tour_cost

'''
Helper function to implement 3-opt neighbourhood search 
'''
def three_separate_segments(n: int):
    """Generate all separate (disconnected) segment combinations"""
    return ((i, j, k)
        for i in range(n)
        for j in range(i + 2, n)
        for k in range(j + 2, n - (i == 0))) # if i == 0, k cannot be n-1, the three segments must be separate

def getCost(tour):
    cost = 0
    for i in range(len(tour)):
        cost += map[tour[i]][tour[(i+1)%len(tour)]]
    return cost

'''
Function to hill climbing algorithm  
'''
def hillClimbing(): 
    root = random.randrange(0,len(map))
    tour = []

    TSPNearest(map, root, tour)
    cost = getCost(tour)

    while True:
        print("The current tour is {}, with a cost of {}.".format(tour, cost))
#       newtour, newtourCost = twoOpt(tour)
        newtour, newtourCost = threeOpt(tour)
#        newtour, newtourCost = twoPairsExchange(tour)
        if newtourCost < cost:                        
            tour = newtour
            cost = newtourCost
        else:
            break

    return tour, cost

'''
Function to generate a graph in the form of an adjecent matrix. 
'''
def generate_graph(num_vertices):
    # initialize adjacency matrix as a nested list of zeros
    graph = [[0 for j in range(num_vertices)] for i in range(num_vertices)]

    # add edges between all pairs of vertices 
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight

    return graph

N = 12
map = generate_graph(N)
tour, cost = hillClimbing()
tour.append(tour[0])
print("The final tour is {}, with a cost of {}.".format(tour, cost))
