import sys
def LCMS(a, b):
    m, n = len(a), len(b)

    # Initialize m x n matrices for increasing and decreasing sequences
    inc_seq = [[0] * n for _ in range(m)]
    dec_seq = [[0] * n for _ in range(m)]

    # map each common element in a and b to its corresponding index in b. the key is the element in b, 
    # the value is a list of indices where that element is present in b (there can be duplicate common elements)
    b_map = {}
    for i, x in enumerate(b):
        if x in b_map:
            b_map[x].append(i)
        else:
            b_map[x] = [i]

    # fill inc_seq with lengths of increasing subsequences ending at position i
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                inc_seq[i][j] = 1  # base case (length of increasing subsequence is 1)
                for k in range(i):
                    if a[k] in b_map: # if there is a common element to the left of i
                        for l in b_map[a[k]]: # look at the indices of the common element in b
                            if l < j and a[k] < a[i] and inc_seq[k][l] + 1 > inc_seq[i][j]: # make sure the index in b is smaller than j and the element is smaller than the one at a[i] (increasing sequence to i)
                                inc_seq[i][j] = inc_seq[k][l] + 1

    # fill dec_seq with lengths of decreasing subsequences starting at position i
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if a[i] == b[j]:
                dec_seq[i][j] = 1  # base case (length of decreasing subsequence is 1)
                for k in range(i+1, m):
                    if a[k] in b_map: # if there is a common element to the right
                        for l in b_map[a[k]]: # look at the indices of the common element in b
                            if l > j and a[k] < a[i] and dec_seq[k][l] + 1 > dec_seq[i][j]: # make sure the index in b is larger than j and the element is smaller than the one at a[i] (decreasing sequence away from i)
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
