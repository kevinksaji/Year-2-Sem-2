'''
p represents the dimensions of the matrixes 
Each number represents the number of rows in the matrix
The first matrix is of dimension 30*35, the second is of dimension 35*15
'''

p = [30, 35, 15, 5, 10, 20, 25] 

'''
In the following code, m[i][j] represents the minimal number of multiplications 
required to compute A(i)*A(i+1)*...*A(j); s[i][j] represents the optimal split 
to compute A(i)*A(i+1)*...*A(j)
'''

# an iterative version

n = len(p) - 1
m = [[0] * (n + 1) for _ in range(n + 1)]
s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    m[i][i] = 0 # base cases
for l in range(2, n + 1): # consider chains of length 2, and then 3, and then 4, and ... 
    for i in range(1, n - l + 2): # i is the starting index of the chain
        j = i + l - 1 # j is the end index of the chain
        m[i][j] = float('inf')
        for k in range(i, j):
            q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j], s[i][j] = q, k

print('iterative MCM: # of multiplication is {0}, split at {1}'.format(m[1][n], s[1][n]))

'''
A recursive version of matrix chain multiplication.
The output is a tuple (a, b) where a is the number of scalar multiplication 
and b is where the split is.
'''

def mcm_recursive(i, j):
    if i == j:
        return 0, -1
    else:
        m = float('inf')
        for k in range(i, j):
            q = mcm_recursive(i, k)[0] + mcm_recursive(k+1, j)[0] + p[i-1] * p[k] * p[j]
            if q < m:
                m, s = q, k
        return m, s

num, split = mcm_recursive(1, 6)
print('recursive MCM: # of multiplication is {0}, split at {1}'.format(num, split))

'''
Another recursive version of matrix chain multiplication.
The output is a tuple (a, b) where a is the number of scalar multiplication 
and b is where the split is.
It relies on two global data structure m and s, which remembers the optimal solutions.
That is, m[i,j] is the optimal number of multiplication for multipying matrxi i to j;
s[i,j] is the optimal first split for multipying matrxi i to j.
'''

n = len(p) - 1
m, s = {(i, i): 0 for i in range(1, n + 1)}, {(i, i): -1 for i in range(1, n + 1)}

def mcm_memoize(i, j):
    if (i, j) in m:
        return m[i,j], s[i,j]
    else:
        m[i,j] = float('inf')
        for k in range(i, j):
            q = mcm_memoize(i, k)[0] + mcm_memoize(k+1, j)[0] + p[i-1] * p[k] * p[j]
            if q < m[i,j]:
                m[i,j], s[i,j] = q, k
        return m[i,j], s[i,j]

num, split = mcm_memoize(1, 6)
print('recursive MCM: # of multiplication is {0}, split at {1}'.format(num, split))
