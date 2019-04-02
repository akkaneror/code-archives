# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
import numpy as np
def partition(arr, low, high):
    index = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            index = index + 1
            arr[index], arr[j] = arr[j], arr[index]

    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSortPartition(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSortPartition(arr, low, pi - 1)
        quickSortPartition(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortPartition(arr, 0, n - 1)
print("Sorted array is:", arr)



# good ol' qsort
def quickSortBasic(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < pivot:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        first_part = quickSortBasic(x[:i])
        second_part = quickSortBasic(x[i + 1:])
        first_part.append(x[i])
        return first_part + second_part

import statistics
def quickSort3Way(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        # recursively call quicksort on gradually smaller and smaller
        return quickSort3Way(less) + equal + quickSort3Way(greater)

    else:
        return array
def quickSort(arr, left, right):
    i = left; j = right
    pivot = arr[np.random.randint(left, right)]
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1; j -= 1

    if left < j:
        quickSort(arr, left, j)
    if i < right:
        quickSort(arr, i, right)

arr2 = np.array([10, 2, 9, 12, -2, 1, 15, 7, 20])
quickSort(arr2, 0, len(arr2) - 1)
print("Sorted Array:", arr2)
