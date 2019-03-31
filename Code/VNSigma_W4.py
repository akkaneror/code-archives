a = int(input())
b = int(input())
count = 0
for i in (a, b):
    if (i % 8 == 0):
        count += 1
print(count)