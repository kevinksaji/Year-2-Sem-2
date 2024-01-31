# Fibonacci Revised

import time

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    fib_number = [1] * (n + 1)
    for i in range(3, n + 1):
        fib_number[i] = fib_number[i-2] + fib_number[i-1]
    return fib_number[n]

fib_memo = {1:1, 2:1}
def fib_memoize(n):
    global fib_memo
    if n in fib_memo:
        return fib_memo[n]
    else:
        fib_memo[n] = fib_memoize(n-1) + fib_memoize(n -2)
        return fib_memo[n]

start_time = time.time()
print(fib_recursive(50))
print('fibanacci recursive takes: %.6g seconds' % (time.time() - start_time))
start_time = time.time()
print(fib_iterative(50))
print('fibanacci iterative takes: %.6g seconds' % (time.time() - start_time))
start_time = time.time()
print(fib_memoize(50))
print('fibanacci memoize takes: %.6g seconds' % (time.time() - start_time))
