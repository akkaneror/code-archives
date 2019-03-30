def findPosition(arr, n, req_sum):
    first_index = 0; last_index = 1; sum = arr[first_index]
    while last_index <= n:
        while sum > req_sum and first_index < last_index - 1:
            sum -= arr[first_index]
            first_index += 1
        if sum == req_sum:
            print(first_index + 1, last_index)
            return 1
        if last_index < n:
            sum += arr[last_index]
        last_index += 1
    print(-1)
    return -1

t = int(input())
for i in range(t):
    n, req_sum = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    findPosition(arr, n, req_sum)