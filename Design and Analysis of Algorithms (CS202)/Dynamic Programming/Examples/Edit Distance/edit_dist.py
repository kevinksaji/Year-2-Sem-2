def edit_dist(s1, s2):
    # implement this function
    # the expected output for the inputs below are 2, 2, 3 respectively
    n, m = len(s1), len(s2)
    dist = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][m] = n - i
    for j in range(m+1):
        dist[n][j] = m - j
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dist[i][j]  = min(dist[i+1][j+1] + (s1[i] != s2[j]), 
                              dist[i+1][j] + 1, # the cell below
                              dist[i][j+1] + 1) # the cell to the right
    
    return dist[0][0]

print(edit_dist('diary', 'binary'))
print(edit_dist('hexagon', 'heptagon'))
print(edit_dist('sleeplessness', 'selflessness'))
