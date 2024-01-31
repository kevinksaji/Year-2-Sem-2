def reorder(A, p, r):
    k = A[r]
    B, C = [], []
    for i in range(p, r):
        if A[i] <= k:
            B.append(A[i])
        else:
            C.append(A[i])
    A[p:r+1] = B + [k] + C
    print(len(B))
    return len(B)

def quicksort(A, p, r):
    if p < r:
        q = reorder(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

A = [3,5,2,7]
quicksort(A, 0, len(A) - 1)
print('result from quicksort:', A)

