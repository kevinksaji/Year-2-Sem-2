# Implement function partition with pivot the last element x = A[r]
# After this function, all elements smaller than or equal to x are on the left side of x,
# and all elements greater than x are on the right side of x
# This function should return the index of the pivot
# There shouldn't be any declaration of lists, dictionaries or sets.

def partition(A, p, r):
    # A is a list, p is the starting index and r is the ending index, both inclusive
    # This function should return the index of the pivot
    x = A[r] # pivot
    i = p - 1 # index of the smaller element
    for j in range(p, r): # iterate through the list
        if A[j] <= x: # if the current element is smaller than or equal to the pivot
            i += 1  # increment index of the smaller element
            A[i], A[j] = A[j], A[i] # swap A[i] and A[j]
    A[i + 1], A[r] = A[r], A[i + 1] # swap A[i + 1] and A[r]
    return i + 1 # return the index of the pivot

# Example usage of the function
A = [2, 8, 7, 1, 3, 5, 6, 4]
print(partition(A, 0, len(A) - 1))  # Output: 3
print(A)  # Output: [2, 1, 3, 4, 7, 5, 6, 8]