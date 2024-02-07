import random

n = 20
W = 150
random.seed('fractional-knapsack')

weight, value = [random.randint(10, 20) for i in range(n)], [random.randint(100, 200) for i in range(n)]

max_value, weight_sum = 0.0, 0.0

value_weight_ratio = [value[i] / weight[i] for i in range(n)]


a = sorted(list(enumerate(value_weight_ratio)), key= lambda x:x[1], reverse=True)

print(a)


i = 0
while weight_sum < W:
    if weight_sum + weight[a[i][0]] <= W:
        weight_sum += weight[a[i][0]]
        max_value += value[a[i][0]]
    else:
        max_value += (W - weight_sum) * value_weight_ratio[a[i][0]]
        weight_sum = W
    i += 1
print('maximum value: %.2f' % max_value)