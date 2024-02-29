import sys

def longest_common_subsequence(a, b):
    m, n = len(a), len(b)

    LCS = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1): #first row are all 0
        LCS[i][0] = 0

    for j in range(n+1): #first column are all 0
        LCS[0][j] = 0

    # start from 1 because the first row and column are already filled with 0 (base case)
    for i in range(1, m+1):
        for j in range(1, n+1): # build LCS[i][j]
            if a[i-1] == b[j-1]: # if the two elements are the same
                LCS[i][j] = LCS[i-1][j-1] + 1 # add 1 to the previous LCS (add 1 to the value in the top left cell of the current cell)
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) # take the maximum of the previous LCS (max of the cell above and the cell beside)

    
    # Backtrack and return the integers in the LCS
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]: # if the two elements are the same
            lcs.append(a[i-1]) # add the element to the LCS
            i -= 1
            j -= 1
        elif LCS[i-1][j] > LCS[i][j-1]: # if the value in the cell above is greater than the value in the cell beside
            i -= 1
        else:
            j -= 1

    # print the list of selected items
    lcs.reverse() # reverse the list of items to get the correct order
    # print('lcs:', lcs)

    return lcs

def compute_LIS(sequence):
    # Function that computes the longest increasing subsequence ending at index i
    # sequence_values[i] is the length of the longest increasing subsequence ending at index i
    
    sequence_values_LIS = [1] * len(sequence)
    for i in range(1, len(sequence)): # iterate from the second element as the first element is already set to 1
        for j in range(i): # iterate from the start of the sequence to the current index
            if sequence[i] > sequence[j]: # element at j has to always be strictly smaller than pivot element at i (increasing sequence from left to right)
                sequence_values_LIS[i] = max(sequence_values_LIS[i], sequence_values_LIS[j] + 1)
    
    return sequence_values_LIS
    
def compute_LDS(sequence):
    # Function that computes the longest decreasing subsequence starting at index i
    # sequence_values[i] is the length of the longest decreasing subsequence starting at index i

    sequence_values_LDS = [1] * len(sequence)
    for i in range(len(sequence)-2, -1, -1): # iterate from the second last element to the first element (last element is already set to 1)
        for j in range(i + 1, len(sequence)): # iterate from the index after i to the end of the sequence
            if sequence[i] > sequence[j]: # element at j has to always be strictly smaller than pivot element at i (decreasing sequence from left to right)
                sequence_values_LDS[i] = max(sequence_values_LDS[i], sequence_values_LDS[j] + 1)
    
    return sequence_values_LDS

def LCMS(a, b):
    lcs = longest_common_subsequence(a, b)
    LIS = compute_LIS(lcs)
    LDS = compute_LDS(lcs)
    max_length = 0
    
    #Iterate over the elements in lcs, and find the longest mountain sequence
    for i in range(len(lcs)):
        # Find the longest mountain sequence with i as the peak
            max_length = max(max_length, LIS[i] + LDS[i] - 1) # -1 because the peak is counted twice
            

    return max_length

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = [int(s, 16) for s in sys.stdin.readline().split()]
    b = [int(s, 16) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
