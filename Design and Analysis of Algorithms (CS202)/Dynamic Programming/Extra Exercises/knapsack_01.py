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
