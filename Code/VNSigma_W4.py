def duplicate_items(list_numbers):
    memory = []
    repeated_lists = []
    for i in range(0, len(list_numbers)):
        if list_numbers[i] in memory:
            repeated_lists.append(list_numbers[i])
        else:
            memory.append(list_numbers[i])

    return repeated_lists

print(duplicate_items([1, 3, 4, 2, 1, 2, 4]))

def flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])//2):
            matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

    return matrix

print(flip_vertical_axis([[1,0,0],[0,0,1]]))

def reverse_string(a_string):
    return a_string[::-1]



myTuple = ("John", "Peter", "Vicky")

x = "".join(myTuple)

print(x)

def reverse_string(a_string):
    str = list(a_string)
    for i in range(len(a_string)//2):
        str[i], str[-i-1] = str[-i-1], str[i]
    return ''.join(str)

print(reverse_string("bread"))