# with a given change, implement an algorithm to compute the minimum number of coins, together with the ways to make up this change. If there are more than 1 way to make up this change, list them all. For example, 11 cents can be made by 2 pieces of 2-cents and 1 piece of 7-cents, or 1 piece of 1-cent, 1 piece of 3-cents and 1 piece of 7-cents, both way give 3 coins
denom = [(1, 2), (2, 2), (5, 2), (10, 2), (20, 1), (50, 1), (100, 2)]

m = len(denom)
n = 300
