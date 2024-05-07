import random

n = 20
W = 150
random.seed('fractional-knapsack')

weight, value = [random.randint(10, 20) for i in range(n)], [random.randint(100, 200) for i in range(n)]

max_value, weight_sum = 0.0, 0.0

value_weight_ratio = [value[i] / weight[i] for i in range(n)]


a = sorted(list(enumerate(value_weight_ratio)), key= lambda x:x[1], reverse=True) # sort the items by value/weight ratio, the item with the highest value/weight ratio is at the beginning of the list

print(a)

# Fractional Knapsack
i = 0 # index of the item
while weight_sum < W: # while the weight of the items in the knapsack is less than the maximum weight
    if weight_sum + weight[a[i][0]] <= W: # if the weight of the item is less than the remaining weight of the knapsack
        weight_sum += weight[a[i][0]] # add the weight of the item to the weight sum
        max_value += value[a[i][0]] # add the value of the item to the maximum value
    else:
        max_value += (W - weight_sum) * value_weight_ratio[a[i][0]] # add the value of the fraction of the item that can fit into the knapsack
        weight_sum = W # set the weight sum to the maximum weight
    i += 1 # move to the next item
print('maximum value: %.2f' % max_value)