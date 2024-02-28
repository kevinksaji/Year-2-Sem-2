import random

random.seed('knapsack')
n = 20
weight = []
for _ in range(n):
    while True:
        i = random.randint(4*n, 6*n)
        if i not in weight:
            weight.append(i)
            break
sum_weight = sum(weight)
value = [0] * n
for i in range(n):
    value[i] = random.randint(5*weight[i], 6*weight[i])

weight_limit = sum_weight // 2

print('generating data...')
print('list of "item:weight:value":')
print(' '.join(['item_'+str(i+1)+':'+str(weight[i])+':'+str(value[i]) for i in range(n)]))
print('knapsack capacity:', weight_limit)

# implement an algorithm to solve the 0/1 knapsack problem
# each item is described by a weight and a value
# first, compute the maximum value without exceeding the knapsack capacity
# second, print the list of selected items.

list_of_items = []
# set the first row and column to 0
max_value = [[0] * (weight_limit+1) for _ in range(n+1)]

# fill the table
for i in range(1, n+1): # item
    for w in range(1, weight_limit+1): # weight
        if weight[i-1] > w:  # if the item is too heavy
            max_value[i][w] = max_value[i-1][w] # you can't take the item
        else:
            max_value[i][w] = max(max_value[i-1][w], max_value[i-1][w-weight[i-1]]+value[i-1])# you take the max of if the item is not taken or if the item is taken

# Backtracking to find the selected items
w = weight_limit
for i in range(n, 0, -1): # start from the last item, all the way to the first item
    if max_value[i][w] != max_value[i - 1][w]: # if the value of the item is not equal to the value of the previous item, it means that the item is taken
        list_of_items.append(i)
        w -= weight[i - 1] # subtract the weight of the item from the weight limit

list_of_items.reverse() # reverse the list of items to get the correct order

# print the maximum value
print('maximum value:', max_value[n][weight_limit])

# print the list of selected items
print('list of selected items:', list_of_items)

