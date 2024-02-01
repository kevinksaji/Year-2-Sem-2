import sys
import math


def gen_comb1(n:int, m:int, p:int, s:str):
    if p == n:
        if m == 0:
            combs.append(s)
    else:
        gen_comb1(n, m-1, p+1, s+char[p]) # with the character s[start]
        gen_comb1(n, m, p+1, s) # skip the character s[start]

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb1(n, m, 0, '')
print(combs)

def gen_comb2(n:int, m:int, p:int, q:int, s:str):
    # n, m: generate all combinations of m from n numbers 0, 1, 2,..., n-1
    # p: from which position to start choosing next integer
    # q: number of remaining numbers to be chosen
    if q == 0:
        combs.append(s)
    else:
        for i in range(p, n-q+1):
            gen_comb2(n, m, i+1, q-1, s+char[i])

char = 'abcdefghij'
n, m, combs = len(char), 3, []
gen_comb2(n, m, 0, m, '')
print(combs)


def p10_lines(n, m, p, q, s, count): # may include other args
    # think about how to print the 1st, 10th, 100th, ... lines only
    # you can use and modify from either recursion function above
    # p: from which position to start choosing next integer
    # q: number of remaining numbers to be chosen
    if q == 0:
        
        combs.append(s)
    else:
        for i in range(p, n-q+1):

            p10_lines(n, m, i+1, q-1, s+char[i], count+1)

num_line = int(sys.stdin.readline())
gn, gc = 0, [[1]]
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    p10_lines(n, m)
