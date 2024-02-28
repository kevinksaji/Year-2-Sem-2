# with a given change, implement an algorithm to compute the minimum number of coins, together with the ways to make up this change. If there are more than 1 way to make up this change, list them all. For example, 11 cents can be made by 2 pieces of 2-cents and 1 piece of 7-cents, or 1 piece of 1-cent, 1 piece of 3-cents and 1 piece of 7-cents, both way give 3 coins
denom = [(1, 2), (2, 2), (5, 2), (10, 2), (20, 1), (50, 1), (100, 2)]

m = len(denom)
n = 300

denom.insert(0, 0) # insert a dummy denomination at the beginning of the list to make the index of the list the same as the index of the denominations

min_coin = [[float('inf')]*(n+1) for i in range(m+1)]  # min_coin[i][j] is the minimum number of coins to make up j cents using the first i denominations

for i in range(m+1):
    min_coin[i][0] = 0 # base case: 0 coins to make up 0 cents

for j in range(1, m+1): # j is the denomination we consider
    for i in range(1, n+1): # i is the amount of cents we want to make up
        for k in range(denom[j][1]+1): # k is the number of coins of the current denomination we use
            if i >= k*denom[j][0]: # if i is greater than or equal to k*denom[j], the current denomination can be used to make up i cents
                min_coin[j][i] = min(min_coin[j][i], k + min_coin[j-1][i-k*denom[j][0]]) # we take the minimum of the current minimum number of coins to make up i cents and k + the minimum number of coins to make up i-k*denom[j] cents

print(min_coin[m][n])