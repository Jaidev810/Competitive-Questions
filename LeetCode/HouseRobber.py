def rob(arr, i, n):
    
    if i+2 >= n:
        return 0, 0
    
    temp = arr[i]
    for j in range(i+2, n):
        further_max = rob(arr[j:], j, n)[0]
        sum = temp + further_max
        

    excluding_max = rob(arr[i:], i, n)[1]
    overall_max = max(sum, excluding_max)

    return sum, overall_max


arr = [1, 2, 3, 1]
print(rob(arr, 0, len(arr)))