def rob(arr):
    maxele = arr[0]

    for i in range(2, len(arr), 2):
        sum = arr[i-2] +arr[i]
        maxele = max(sum, maxele)
    
    for i in range(1, len(arr), 2):
        sum = arr[i-2] + arr[i]
        maxele = max(sum, maxele)

    return maxele



arr = [2, 1, 1, 2]
maxele = rob(arr)
print(maxele)