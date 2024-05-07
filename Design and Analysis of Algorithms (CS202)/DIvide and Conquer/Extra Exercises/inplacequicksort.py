def quicksort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Select the rightmost element as pivot
    pivot = arr[high]

    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] < pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the position from where partition is done
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array:", arr)