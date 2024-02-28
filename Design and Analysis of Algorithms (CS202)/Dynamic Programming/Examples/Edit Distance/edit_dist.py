def edit_dist(s1, s2):
    # implement this function
    # the expected output for the inputs below are 2, 2, 3 respectively
    n, m = len(s1), len(s2) # get the length of the two strings
    dist = [[0] * (m+1) for _ in range(n+1)] # create a 2D array of size (n+1) x (m+1)

    for i in range(n+1):
        dist[i][m] = n - i # fill the last column with the difference between the length of the two strings
    for j in range(m+1):
        dist[n][j] = m - j # fill the last row with the difference between the length of the two strings

    for i in range(n-1, -1, -1): # start from the second last row, 2nd parameter means stop at -1, 3rd parameter means step by -1

        for j in range(m-1, -1, -1): # start from the second last column, 2nd parameter means stop at -1, 3rd parameter means step by -1
            if s1[i] != s2[j]:
                dist[i][j] = min(dist[i+1][j] + 1, dist[i][j+1] + 1, dist[i+1][j+1] + 1) # if the two elements are not the same, take the minimum of the three values (bottom + 1, right + 1, bottom right + 1)
            else:
                dist[i][j] = min(dist[i+1][j] + 1, dist[i][j+1] + 1, dist[i+1][j+1]) # if the two elements are the same, take the minimum of the three values(bottom + 1, right + 1, bottom right + 0)

            # alternate to the if else statements
                # dist[i][j] = min(dist[i+1][j] + 1, dist[i][j+1] + 1, dist[i+1][j+1]) + (s1[i] != s2[j])
    return dist[0][0]

print(edit_dist('diary', 'binary'))
print(edit_dist('hexagon', 'heptagon'))
print(edit_dist('sleeplessness', 'selflessness'))
