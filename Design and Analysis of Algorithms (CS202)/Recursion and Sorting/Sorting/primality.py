import math, time

def naive(upper_bound):
    prime = [2]
    # i: for all odd numbers less than upper_bound
        # j: for all odd numbers less than i
            if i % j == 0:
                break # why break?
        else:
            prime.append(i)
    return prime

def improved(upper_bound): 
    prime = [2]
    for i in range(3, upper_bound, 2):
        found = False # why need a variable found
        # complete the implementation here
        if not found:
            prime.append(i)
    return prime

def sieve(upper_bound):
    flag = # all numbers are initially considered potentially prime
    prime = []
    for i in range(2, upper_bound + 1):
        if flag[i]:
            # i's multiples, e.g., 2*i, 3*i, ... are not primes
            prime.append(i)
    return prime

def print_prime(prime):
    if len(prime) < 9:
        print('the list of prime:', prime)
    else:
        print('the list of prime: [%s]' % ', '.join([str(i) for i in prime[:4]] + ['...'] + [str(i) for i in prime[-4:]]))

if __name__ == '__main__':
    while True:
        upper_bound = int(input('Type an upper bound (a positive integer) to try: '))
        if upper_bound > 0:
            break
    print('upper bound is', upper_bound)
    print('-- naive --')
    start = time.time()
    primes = naive(upper_bound)
    print('  -- %.6f seconds' % (time.time() - start))
    print_prime(primes)
    print('-- improved --')
    start = time.time()
    primes = improved(upper_bound)
    print('  -- %.6f seconds' % (time.time() - start))
    print_prime(primes)
    print('-- sieve --')
    start = time.time()
    primes = sieve(upper_bound)
    print('  -- %.6f seconds' % (time.time() - start))
    print_prime(primes)
