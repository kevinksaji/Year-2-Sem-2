import sys
import math
from math import factorial


# def gen_comb1(n:int, m:int, p:int, s:str):
#     if p == n:
#         if m == 0:
#             combs.append(s)
#     else:
#         gen_comb1(n, m-1, p+1, s+char[p]) # with the character s[start]
#         gen_comb1(n, m, p+1, s) # skip the character s[start]

# char = 'abcdefghij'
# n, m, combs = len(char), 3, []
# gen_comb1(n, m, 0, '')
# print(combs)

# def gen_comb2(n:int, m:int, p:int, q:int, s:str):
#     # n, m: generate all combinations of m from n numbers 0, 1, 2,..., n-1
#     # p: from which position to start choosing next integer
#     # q: number of remaining numbers to be chosen
#     if q == 0:
#         combs.append(s)
#     else:
#         for i in range(p, n-q+1):
#             gen_comb2(n, m, i+1, q-1, s+char[i])

# char = 'abcdefghij'
# n, m, combs = len(char), 3, []
# gen_comb2(n, m, 0, m, '')
# print(combs)


def count_combinations(n, q):
    if n < 0 or q < 0 or n < q:
        # Handle the error or return a default value like 0
        return 0
    return factorial(n) // (factorial(q) * factorial(n - q))

def p10_lines_recursive(n, m, comb='', start=0, next_power_of_10=1, current_count=[0]):
    # Check if we have a combination of the required length
    if len(comb) == m:
        current_count[0] += 1  # Increment the combination count
        # Print and update the next power of 10 if the current count matches
        if current_count[0] == next_power_of_10:
            print(','.join(map(str, comb)))  # Print the current combination
            return next_power_of_10 * 10  # Return the next power of 10
        return next_power_of_10  # Otherwise, just return the current next power of 10

    # Iterate over the range to generate combinations
    for i in range(start, n):
        # Calculate the remaining spots to fill in the combination
        remaining = m - len(comb)
        # Calculate the number of combinations that can be made with the remaining spots
        remaining_combinations = count_combinations(n - i - 1, remaining - 1)
        # Check if the current count + possible combinations is enough to reach the next power of 10
        if current_count[0] + remaining_combinations >= next_power_of_10:
            # Recursive call with the new prefix, updating the start, and the next power of 10
            next_power_of_10 = p10_lines_recursive(n, m, comb + (i,), i + 1, next_power_of_10, current_count)
        else:
            # If not enough combinations can be made, just update the current count
            current_count[0] += remaining_combinations

    return next_power_of_10  # Return the next power of 10 for the caller

def p10_lines(n, m):
    # Call the recursive function with initial values
    p10_lines_recursive(n, m, comb=(), start=0, next_power_of_10=1, current_count=[0])

num_line = int(sys.stdin.readline())
gn, gc = 0, [[1]]
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m = a[0], a[1]
    p10_lines(n, m)
