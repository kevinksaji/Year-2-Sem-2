A = ['in', 'park', 'several', 'kid', 'play', 'soccer']
B = ['park', 'his', 'car', 'before', 'watch', 'play']

# A = ['ant', 'cat', 'bee', 'dog', 'elk', 'fox']
# B = ['bee', 'ant', 'cat', 'fox', 'elk']

m, n = len(A), len(B)

LCS = [[None] * (n+1) for _ in range(m+1)]

# write your code here
# the expected output for the above input is 2.

for i in range(n+1):
    LCS[i][0] = 0
for j in range(m+1):
    LCS[0][j] = 0

for i in range(1, m+1):
    for j in range(1, n+1): # build LCS[i][j]
        if A[i-1] == B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[m][n])
