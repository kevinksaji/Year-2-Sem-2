import sys

def binary_search(sub, val):
    """Helper function to perform binary search on the subsequence."""
    left, right = 0, len(sub) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sub[mid] == val:
            return mid
        elif sub[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left

def LCMS(A, B):
    
    
    # Map each number to its indices in B
    indices_in_B = {}
    for i, b in enumerate(B):
        indices_in_B[b] = i  # We only keep the last occurrence as we're looking for the peak

    # Filter A to contain only elements also in B and track the first occurrence
    A_filtered = []
    indices_in_A = {}
    for idx, a in enumerate(A):
        if a in indices_in_B and a not in indices_in_A:
            A_filtered.append(a)
            indices_in_A[a] = idx  # We only keep the first occurrence as we're looking for the peak

    n = len(A_filtered)
    
    # Initialize the lists to store the longest subsequence lengths
    lis = [0] * n
    lds = [0] * n

    # Initialize the lists to store the actual subsequences for binary search
    lis_tails = [-1] * n
    lds_tails = [-1] * n
    lis_length = 0
    lds_length = 0

    # Calculate the LIS for the filtered A
    for i, a in enumerate(A_filtered):
        idx = binary_search(lis_tails, a, lis_length)
        lis_tails[idx] = a
        lis_length = max(lis_length, idx + 1)
        lis[i] = idx + 1

    # Calculate the LDS for the filtered A in reverse
    for i, a in enumerate(reversed(A_filtered)):
        idx = binary_search(lds_tails, a, lds_length)
        lds_tails[idx] = a
        lds_length = max(lds_length, idx + 1)
        lds[n - 1 - i] = idx + 1

    # Find the length of the LCMS using LIS and LDS
    max_lcms = 0
    for i in range(n):
        a = A_filtered[i]
        if lis[i] > 1 and lds[i] > 1:  # Valid mountain must be strictly increasing and then decreasing
            max_lcms = max(max_lcms, lis[i] + lds[i] - 1)

    return max_lcms

# We will test the function with actual data after finalizing the implementation.


num_pair = int(sys.stdin.readline())
for _ in range(num_pair):
    a = [int(s, 16) for s in sys.stdin.readline().split()]
    b = [int(s, 16) for s in sys.stdin.readline().split()]
    print(LCMS(a, b))
