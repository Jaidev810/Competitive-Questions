def rob(arr):
    max = 0
    sum = 0

    for i in range(0, len(arr), 2):
        sum = sum + arr[i]

    if max < sum:
        max = sum

    sum = 0
    
    for i in range(1, len(arr), 2):
        sum = sum + arr[i]

    if max < sum:
        max = sum

    return max

arr = [1, 2, 3, 1]
print(rob(arr))