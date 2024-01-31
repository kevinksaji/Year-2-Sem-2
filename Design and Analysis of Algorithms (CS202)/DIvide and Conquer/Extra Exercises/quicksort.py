'''
The following implements the so-called Lomuto Partition Scheme
A demo is available at: https://www.youtube.com/watch?v=86WSheyr8cM
'''

import random
random.seed('quicksort')

A = [random.randint(1, 1000) for _ in range(100)]
random.shuffle(A)

def partition(A, p, r):
    k, i = A[r], p-1
    for j in range(p, r):
        if A[j] <= k:
            i+=1
            A[i], A[j] = A[j], A[i]
        
    i+= 1
    A[i], A[r] = k, A[i]
    return i
            
            

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

quicksort(A, 0, len(A) - 1)
print('result from quicksort:', A)

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

random.shuffle(A)
randomized_quicksort(A, 0, len(A) - 1)
print('result from randomized_quicksort:', A)
