import sys

def bounded_knapsack(weight, value, quantity, limit):
    n = len(weight) # number of items

    max_value = [[0] * (limit+1) for _ in range(n+1)] # initialise max_value table

    # fill the table
    for i in range(1, n + 1): # iterate over the different items
            for w in range(1, limit + 1): # iterate over the maximum weights
                    # iterate over each possible quantity q
                    # start from 0 to consider scenario where the item is not used
                    # when q = 0, max_value[i][w] will just be max_value[i-1][w]
                    for q in range(0, quantity[i-1] + 1): 
                        if q * weight[i-1] <= w:
                            # take the max of the current value at max_value[i][w] and the value of the scenario where q items are used
                            max_value[i][w] = max(max_value[i][w], max_value[i-1][w - weight[i-1] * q]+ q * value[i-1])
                        else:
                            break
                        
    return max_value[n][limit]


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
    print(bounded_knapsack([i[0] for i in a[:-1]], [i[1] for i in a[:-1]], [i[2] for i in a[:-1]], a[-1][0]))

# The time complexity is O(n * limit * max(quantity)) because we have 3 nested loops. 
# The outermost loop iterates over the different items, the second loop iterates over the maximum weights, 
# and the innermost loop iterates over the possible quantities. 
# The outermost loop iterates over n items, the second loop iterates over the maximum weights, 
# and the innermost loop iterates over the possible quantities. Therefore, the time complexity is O(n * limit * max(quantity)).
