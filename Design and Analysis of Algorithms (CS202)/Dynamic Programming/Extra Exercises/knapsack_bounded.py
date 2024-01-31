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
