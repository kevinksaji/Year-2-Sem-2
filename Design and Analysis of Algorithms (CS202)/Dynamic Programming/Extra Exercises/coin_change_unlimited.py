# implement an algorithm to compute the minimum number of coins to make up a given change, assuming the supply of coins for each denomination are unlimited

denom = [1, 3, 4]
m = len(denom)
n = 6

# with denomination [1, 3, 4] cents, what is the minimum number of coins to make up 30 cents?

min_coin = [float('inf')] * (n+1)  # min_coin[i] is the minimum number of coins to make up i cents

min_coin[0] = 0 # base case: 0 coins to make up 0 cents

for i in range(1, n+1): # i is the amount of cents we want to make up
    for j in range(m): # denom[j is the denomination we consider
        if i >= denom[j]: # if i is greater than or equal to the denomination, the denomination can be used to make up i cents
            min_coin[i] = min(min_coin[i], 1 + min_coin[i-denom[j]]) # we take the minimum of the current minimum number of coins to make up i cents and 1 + the minimum number of coins to make up i-denom[j] cents
    
for i in range (n+1):
    print(i, min_coin[i])
