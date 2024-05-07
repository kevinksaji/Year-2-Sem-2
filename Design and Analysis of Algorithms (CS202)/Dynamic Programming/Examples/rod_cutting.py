rod_price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# a recursive version without memoization

def rod_cutting_recursive(n):
    if n == 0: # base case
        return 0
    q = 0 # max revenue
    for i in range(1, min(n+1, len(rod_price))): #
        q = max(q, rod_price[i] + rod_cutting_recursive(n-i)) # every iteration, we cut the rod at length i and find the max revenue
    return q

print(rod_cutting_recursive(6))

# an iterative version

n = len(rod_price)
max_price = [0] * n # array to store the max revenue for each rod length
first_cut = [0] * n # array to store the first cut for each rod length

def rod_cutting_iterative():
    for i in range(1, n): # start from rod length 1 and find the max revenue for each rod length to use in the next iteration as the optimal solution
        for j in range(1, min(i+1, len(rod_price))): # for each rod length, find the max revenue by cutting the rod at length j
            new_price = rod_price[j] + max_price[i-j] # max revenue for rod length i is the max of the current max revenue and the revenue from cutting the rod at length j, and adding the revenue from the remaining rod length i-j
            if new_price > max_price[i]:
                max_price[i] = new_price
                first_cut[i] = j

rod_cutting_iterative()
print('max_price:', max_price)
print('first_cut:', first_cut)

# a recursive version with memoization

def rod_cutting_recursive_memo(n, memo):
    if n == 0:
        return 0
    
    if n in memo:
        return memo[n]

    q = 0
    for i in range(1, min(n+1, len(rod_price))): 
        q = max(q, rod_price[i] + rod_cutting_recursive_memo(n-i, memo))
    
    memo[n] = q
    return q

print(rod_cutting_recursive_memo(6, {}))
