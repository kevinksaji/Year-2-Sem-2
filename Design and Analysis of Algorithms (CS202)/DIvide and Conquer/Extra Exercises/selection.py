import random
random.seed('quicksort')

A = [random.randint(1, 1000) for _ in range(100)]
random.shuffle(A)

def partition(A, p, r):
    # implement partition in class exercise
    # and then copy-paste here

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q] 
    if i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)

print(randomized_select(A, 0, len(A)-1, 6))
