denom = [(1, 2), (2, 2), (5, 2), (10, 2), (20, 1), (50, 1), (100, 2)]

m = len(denom)
n = 300

denom.insert(0, 0) # insert at position 0, so that each row i considers using denom[i] (cents: denom[i][0]; limit: denom[i][1])
min_coin = [[float('inf')] * (n+1) for _ in range(m+1)]
for i in range(m+1):
    min_coin[i][0] = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if denom[i][1] > 0: # if denom[i] is still available
            min_coin[i][j] = min(min_coin[i-1][j], min_coin[i][j-denom[i][0]] + 1)
        else: # if denom[i] is not available
            min_coin[i][j] = min_coin[i-1][j]

print(min_coin[m][n])
