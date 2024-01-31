# implement an algorithm to compute the minimum number of coins to make up a given change, assuming the supply of coins for each denomination are unlimited

denom = [1, 3, 4]
m = len(denom)
n = 30

# with denomination [1, 3, 4] cents, what is the minimum number of coins to make up 30 cents?

min_coin = [float('inf')] * (n+1)

# this is the base case
min_coin[0] = 0

for i in range(n+1):
    for j in range(m): # each time consider denomination denom[j]
        if i>=denom[j]:
            if min_coin[i-denom[j]]+1 < min_coin[i]:
                min_coin[i] = min_coin[i-denom[j]]

        
    #use sub-prob (i - denom[0])
    #use sub-prob (i - demnm[1])
    #use sub-prob (i - denom[2])
    for i in range(1, n+1):
        print(i, 'cents:', min_coin[i], 'coins')
