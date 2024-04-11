# Python3 program to solve
# Traveling Salesman Problem using
import math
import random

maxsize = float('inf')

# This function sets up final_path
def TSPNearest(map, start, tour):
	tour.append(start)

	nearestDistance = maxsize
	nearestCity = -1
	for i in range(len(map)):
		if not(i in tour) and map[start][i] < nearestDistance:
			nearestCity = i
			nearestDistance = map[start][i]

	if nearestCity == -1:
		return
	else:
		TSPNearest(map, nearestCity, tour)

def twoOpt(tour):
    bestNeighbour = tour
    bestNeighbourCost = getCost(tour)

    for i in range(0, len(tour)):
        for j in range(0, len(tour)):
            if i != j:
                newtour = tour.copy()
                newtour[i] = tour[j]
                newtour[j] = tour[i]
                newCost = getCost(newtour)
                if newCost < bestNeighbourCost:
                    bestNeighbourCost = newCost
                    bestNeighbour = newtour

    return bestNeighbour, bestNeighbourCost

def getCost(tour):
    cost = 0
    tour.append(tour[0])
    for i in tour:
        cost += map[tour[i]][tour[i+1]]

    tour.pop()
    return cost

'''
Function to hill climbing algorithm  
'''
def hillClimbing(): 
    root = random.randint(0,len(map)-1)
    tour = []

    TSPNearest(map, root, tour)
    cost = getCost(tour)

    while True:
        print("The current tour is {}, with a cost of {}.".format(tour, cost))
        newtour, newtourCost = twoOpt(tour)
        if newtourCost < cost:                        
            tour = newtour
            cost = newtourCost
        else:
            break

    return tour, cost

def simulatedAnnealing(): 
    root = random.randint(0,len(map)-1)
    tour = []
    T = 1
    Tmin = 0.0001
    alpha = 0.9

    TSPNearest(map, root, tour)
    cost = getCost(tour)

    while T > Tmin:
        print("The current tour is {}, with a cost of {}.".format(tour, cost))
        newtour, newtourCost = twoOpt(tour)
        if newtourCost < cost:                        
            tour = newtour
            cost = newtourCost
        else:
            delta = newtourCost - cost # Difference in cost
            if random.random() < math.exp(-delta/T): # Probability of accepting the worse solution
                tour = newtour # Accept the worse solution
                cost = newtourCost # Update the cost
    
        T *= alpha  # Decreases T, cooling phase

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

N = 25
map = generate_graph(N)

print("Trying hill climbing")
tour, cost = hillClimbing()
tour.append(tour[0])
print("The final tour is {}, with a cost of {}.".format(tour, cost))

print()
print("Trying simulated annealing")
tour, cost = simulatedAnnealing()
tour.append(tour[0])
print("The final tour is {}, with a cost of {}.".format(tour, cost))

