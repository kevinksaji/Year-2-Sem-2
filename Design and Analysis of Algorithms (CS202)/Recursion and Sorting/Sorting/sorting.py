def insertion_sort(A):
    # A is a list of numbers
    # write your own code to implement insertion sort
    for i in range(1, A[i]):
        key = A[i]
        j = i-1
        while(A[i] < A[j] and j>= 0):
            A[j+1] = A[j]
            j -= 1
            A[j+1] = key


# ---- with compare_count and assign_count ----
def insertion_sort_with_counts(A):
    # modify insertion sort, so that you can count the number of comparison and the number of assignments
    compare_count = 0
    assign_count = 0

    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        compare_count += 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
            assign_count += 1
            compare_count += 1
        A[j + 1] = key
        assign_count += 1

    return compare_count, assign_count

def merge_sort(A):
    # A is a list of numbers
    # write your own code to implement merge sort with recursion
    if len(A) > 1:
        # Divide the array into two halves
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        # Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1

# ---- with compare_count and assign_count ----
def merge_sort_with_counts(A):
    # modify merge sort, so that you can count the number of comparison and the number of assignments
    compare_count = 0
    assign_count = 0

    if len(A) > 1:
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        # Recursively sort each half and count comparisons and assignments
        compare_count_left, assign_count_left = merge_sort_with_counts(left_half)
        compare_count_right, assign_count_right = merge_sort_with_counts(right_half)

        # Update counts with counts from recursive calls
        compare_count += compare_count_left + compare_count_right
        assign_count += assign_count_left + assign_count_right

        i = j = k = 0

        # Merge the sorted halves and count comparisons and assignments
        while i < len(left_half) and j < len(right_half):
            compare_count += 1
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
            assign_count += 1

        # Copy the remaining elements and count assignments
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1
            assign_count += 1

        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
            assign_count += 1

    return compare_count, assign_count
