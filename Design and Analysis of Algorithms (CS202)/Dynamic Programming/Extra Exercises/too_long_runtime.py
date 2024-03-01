import sys
def LCMS(a, b):
    m, n = len(a), len(b)

    # Initialize m x n matrices for increasing and decreasing sequences
    inc_seq = [[0] * n for _ in range(m)]
    dec_seq = [[0] * n for _ in range(m)]

    # Fill inc_seq with lengths of increasing subsequences ending at position i
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]: # If the element is common in a and b, it can be part of the increasing sequence
                inc_seq[i][j] = 1  # Base case (length of increasing subsequence is 1)
                for k in range(i): 
                    for l in range(j):
                        if a[k] == b[l] and a[k] < a[i] and b[l] < b[j] and inc_seq[k][l] + 1 > inc_seq[i][j]:# If a smaller common element is found in a and b at position k, l (left and above the current position)
                            inc_seq[i][j] = inc_seq[k][l] + 1

    # Fill dec_seq with lengths of decreasing subsequences starting at position i
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if a[i] == b[j]: # If the element is common in a and b, it can be part of the decreasing sequence
                dec_seq[i][j] = 1  # Base case (length of decreasing subsequence is 1)
                for k in range(i+1, m):
                    for l in range(j+1, n):
                        if a[k] == b[l] and a[k] < a[i] and b[l] < b[j] and dec_seq[k][l] + 1 > dec_seq[i][j]: # If a smaller common element is found in a and b at position k, l (right and below the current position)
                            dec_seq[i][j] = dec_seq[k][l] + 1

    # Compute LCMS
    max_length = 0 # Initialise max length of the mountain sequence
    
    for i in range(m):
        for j in range(n):
            if a[i] == b[j] and inc_seq[i][j] > 1 and dec_seq[i][j] > 1: # If the element is part of both an increasing and decreasing sequence
                max_length = max(max_length, inc_seq[i][j] + dec_seq[i][j] - 1) # -1 because the peak element is counted twice

    return max_length

num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = [int(s, 16) for s in sys.stdin.readline().split()]
    b = [int(s, 16) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
