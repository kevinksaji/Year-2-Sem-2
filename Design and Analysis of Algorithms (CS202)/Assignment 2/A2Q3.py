import random

# random generate 10 denominations
# the next denomination ~= the previous * 2, or plus/minus 1
# for each denomination, generate a quantity between 10 and 20 inclusive

random.seed('coin')
curr = 1
denom = [(curr, random.randint(10, 20))]
for i in range(9):
    curr = 2 * curr + 1 - random.randrange(3)
    denom.append((curr, random.randint(10, 20)))
print(denom)

# solution to each subproblem, contain (1) the min number of coins, and (2) all plans with sum of coins being the min num of coins, this is because there is limited supply for each coin, one plan of x cents may allow us to reach x+5 cents, another plan may allow us to reach x+10 cents, depending on whether we have extra coins of 5 cents or 10 cents

class MinCoin:
    def __init__(self, n, p):
        self.num_coin = n
        self.plan = [p]
    def add_plan(self, p):
        self.plan.append(p)

m = len(denom)
n = 2000

min_coin_with_plan = [None] * (n + 1)
min_coin_with_plan[0] = MinCoin(0, [0] * m)
for i in range(m): # suppose we already have solutions using denom[0], denom[1], ..., denom[i-1], now we consider using denom[i]
    for j in range(1, n+1): # consider the min coin problem with sum j cents
        if j >= denom[i][0] and min_coin_with_plan[j - denom[i][0]] is not None: # is it possible to use denom[i][0]? if yes, we can make up j cents by putting 1 coin of denom[i][0] and the min coin solution for j-denom[i][0]
            for p in min_coin_with_plan[j - denom[i][0]].plan: # for each possible plan of making j-denom[i][0]
                if p[i] < denom[i][1]: # now I have a better solution, build a new obj as a solution for j
                    if min_coin_with_plan[j] is None or min_coin_with_plan[j - denom[i][0]].num_coin + 1 < min_coin_with_plan[j].num_coin: # must check if there is enough supply of denom[i][0]
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j] = MinCoin(min_coin_with_plan[j - denom[i][0]].num_coin + 1, p_new)
                    elif min_coin_with_plan[j - denom[i][0]].num_coin + 1 == min_coin_with_plan[j].num_coin: # now I have an equally good solution, only need to add the plan
                        p_new = p.copy()
                        p_new[i] += 1 # add one coin of denom[i][0]
                        min_coin_with_plan[j].add_plan(p_new)

'''
# may print out and check
for i in range(1, n+1):
    if min_coin_with_plan[i] is not None:
        print(i, min_coin_with_plan[i].num_coin, min_coin_with_plan[i].plan)
'''

# if we only consider the minimum number of coins without considering the plans

min_coin_num_only = [[float('inf')] * (n+1) for _ in range(m+1)]
for i in range(m+1):
    min_coin_num_only[i][0] = 0
for i in range(m):
    for j in range(1, n+1):
        min_coin_num_only[i+1][j] = min_coin_num_only[i][j] # if do not use denom[i][0] cents
        for k in range(1, denom[i][1]+1): # using k pieces of denom[i][0] cents
            if j >= k * denom[i][0]:
                min_coin_num_only[i+1][j] = min(min_coin_num_only[i+1][j], min_coin_num_only[i][j - k*denom[i][0]] + k)

# Can array min_coin_num_only be changed to a 1-dimensional array?

all_same = True
for i in range(1, n+1):
    if min_coin_with_plan[i].num_coin != min_coin_num_only[m][i]:
        print('inconsistent result:', min_coin_with_plan[i].num_coin, min_coin_num_only[m][i])
        all_same = False
if all_same:
    print('all the same')

# Now we try another example

random.seed('coin')
curr = 1
denom = [(curr, random.randint(2, 3))]
for i in range(5):
    curr = 2 * curr + 1 - random.randrange(3)
    denom.append((curr, random.randint(2, 3)))
print('another set of denomations:', denom)
# should be [(1, 2), (2, 2), (3, 2), (7, 3), (14, 3), (29, 2)]

n = 100
