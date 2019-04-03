from pygorithm import sorting
import numpy as np
import statistics
main_array = np.array([10, 2, 9, 12, -2, 1, 15, 7, 20])
qs_array = np.copy(main_array)
ms_array = np.copy(main_array).tolist()

'''
Quick Sort in one method
'''
def quickSort(arr, left, right):
    i = left; j = right;
    pivot = statistics.median([arr[0], arr[np.random.randint(left, right)], arr[-1]])
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
'''
Merge Sort with Helper method
'''
def mergeSortHelper(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2

    left_arr = mergeSortHelper(arr[:middle])
    right_arr = mergeSortHelper(arr[middle:])

    return merge(left_arr, right_arr)
'''
Helper method of Merge Sort
'''
def merge(left_arr, right_arr):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    result += left_arr[i:]
    result += right_arr[j:]

    return result

'''
Merge Sort in one method
'''
def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        
        mergeSort(left_arr)
        mergeSort(right_arr)

        i = j = index = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[index] = left_arr[i]
                i += 1
            else:
                arr[index] = right_arr[j]
                j += 1
            index += 1
        arr[index:] = left_arr[i:]
        arr[index:] += right_arr[j:]
        '''
        those 2 lines are similar to this
        while i < len(left_arr): 
            arr[index] = left_arr[i] 
            i += 1
            index += 1
          
        while j < len(right_arr): 
            arr[index] = right_arr[j] 
            j += 1
            index += 1
        '''

    else:
        return arr

quickSort(qs_array, 0, len(qs_array) - 1)
print("Quick Sort:", qs_array)
#print("Merge Sort", mergeSortHelper(ms_array))
mergeSort(ms_array)
print("Merge Sort:", ms_array)
