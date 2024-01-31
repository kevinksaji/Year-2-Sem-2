import time, random
random.seed('binary')
s = set()
while len(s) < 10000:
    s.add(random.randint(1, 1000000))
A = sorted(list(s))

def sequencial_search(key, A):
    for i in range(len(A)):
        if key == A[i]:
            return i
        elif key < A[i]:
            return -1
    return -1

def binary_search(key, A, lower, upper):
    if lower >= upper:
        return -1
    mid = (lower + upper) // 2
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(key, A, lower, mid)
    else:
        return binary_search(key, A, mid + 1, upper)

len_B = 100000
B = [random.randint(1, 1000000) for _ in range(len_B)]

start_time = time.time()
for i in range(len_B):
    sequencial_search(B[i], A)
print('sequencial search takes %.3f seconds' % (time.time() - start_time))

start_time = time.time()
for i in range(len_B):
    binary_search(B[i], A, 0, len(A))
print('binary search takes %.3f seconds' % (time.time() - start_time))