rod_price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# a recursive version without memoization

def rod_cutting_recursive(n):
    if n == 0:
        return 0
    q = 0
    for i in range(1, min(n+1, len(rod_price))): 
        q = max(q, rod_price[i] + rod_cutting_recursive(n-i))
    return q

print(rod_cutting_recursive(6))

# an iterative version

n = len(rod_price)
max_price = [0] * n
first_cut = [0] * n

def rod_cutting_iterative():
    for i in range(1, n):
        for j in range(1, min(i+1, len(rod_price))): 
            new_price = rod_price[j] + max_price[i-j]
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
