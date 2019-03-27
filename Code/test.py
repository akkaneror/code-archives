# qsort with partition
def quickSortPartition(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1


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


quickSortBasic([6, 4, 7, 1, 2, 9, 12, 3])

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSortPartition(alist)
print(alist)
