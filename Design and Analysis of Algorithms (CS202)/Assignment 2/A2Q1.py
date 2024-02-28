import sys

def bounded_knapsack(weight, value, quantity, limit):
    n = len(weight)
    return sum([value[i] * quantity[i] for i in range(n)])

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()]
    print(bounded_knapsack([i[0] for i in a[:-1]], [i[1] for i in a[:-1]], [i[2] for i in a[:-1]], a[-1][0]))
