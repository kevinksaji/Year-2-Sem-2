import random

random.seed('knapsack')
n = 10
weight = []
for _ in range(n):
    while True:
        i = random.randint(4*n, 6*n)
        if i not in weight:
            weight.append(i)
            break
value, quantity, sum_weight = [0] * n, [0] * n, 0
for i in range(n):
    value[i] = random.randint(5*weight[i], 6*weight[i])
    quantity[i] = random.randint(n, 2*n)
    sum_weight += weight[i] * quantity[i]

weight_limit = sum_weight // 2

print('generating data...')
print('list of "weight:value:quantity":')
print(' '.join(['item_'+str(i+1)+':'+str(weight[i])+':'+str(value[i])+':'+str(quantity[i]) for i in range(n)]))
print('knapsack capacity:', weight_limit)

# implement an algorithm to solve the bounded knapsack problem
# each item is described by a weight, a value and its quantity
# unlike the usual setting of bounded knapsack problem, this problem is more specific to allow different quantity bound for each item
# compute the maximum value without exceeding the knapsack capacity and the quantity constraints, and print the list of selected items with their quantities.

# set the first row and column to 0
max_value = [[0] * (weight_limit+1) for _ in range(n+1)]

# fill the table
for i in range(1, n + 1): # item
        for w in range(1, weight_limit + 1): # weight
            for q in range(min(quantity[i - 1] + 1, w // weight[i - 1] + 1)):  # iterate over each possible quantity
                if weight[i - 1] * q <= w:  # Check if the total weight is within the limit
                    max_value[i][w] = max(max_value[i][w], max_value[i - 1][w - weight[i - 1] * q] + value[i - 1] * q)

print(max_value[n][weight_limit])

# Backtracking to find the selected items and the quantity of each selected item
w = weight_limit
selected_items = []
for i in range(n, 0, -1): # start from the last item, all the way to the first item
    for q in range(min(quantity[i - 1] + 1, w // weight[i - 1] + 1)):  # iterate over each possible quantity
        if max_value[i][w] == max_value[i - 1][w - weight[i - 1] * q] + value[i - 1] * q:  # if the value of the item is equal to the value of the previous item plus the value of the current item, it means that the item is taken
            selected_items.append((i, q))
            w -= weight[i - 1] * q  # subtract the weight of the item from the weight limit
            break

# print the list of selected items
print('list of selected items:', selected_items)

# Time complexity: O(n*W*Q), where n is the number of items, W is the weight limit, and Q is the maximum quantity of an item

