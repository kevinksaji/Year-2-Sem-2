# A = ['in', 'park', 'several', 'kid', 'play', 'soccer']
# B = ['park', 'his', 'car', 'before', 'watch', 'play']

# A = ['ant', 'cat', 'bee', 'dog', 'elk', 'fox']
# B = ['bee', 'ant', 'cat', 'fox', 'elk']

A = ['2','2','7','8','5','6','4','1']
B = ['5','2','2','8','6','4','7','1']

m, n = len(A), len(B)

LCS = [[0] * (n+1) for _ in range(m+1)] #

# write your code here
# the expected output for the above input is 2.

for i in range(n): #first row are all 0
    LCS[i][0] = 0

for j in range(m): #first column are all 0
    LCS[0][j] = 0

# start from 1 because the first row and column are already filled with 0 (base case)
for i in range(1, m+1):
    for j in range(1, n+1): # build LCS[i][j]
        if A[i-1] == B[j-1]: # if the two elements are the same
            LCS[i][j] = LCS[i-1][j-1] + 1 # add 1 to the previous LCS (add 1 to the value in the top left cell of the current cell)
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) # take the maximum of the previous LCS (max of the cell above and the cell beside)

print(LCS[m][n])



# Backtrack to print the elements of the LCS
i, j = m, n
lcs = []
while i > 0 and j > 0:
    if A[i-1] == B[j-1]: # if the two elements are the same
        lcs.append(A[i-1]) # add the element to the LCS
        i -= 1
        j -= 1
    elif LCS[i-1][j] > LCS[i][j-1]: # if the value in the cell above is greater than the value in the cell beside
        i -= 1
    else:
        j -= 1

print("lcs")
print(' '.join(lcs[::-1])) # print the LCS in the correct order
