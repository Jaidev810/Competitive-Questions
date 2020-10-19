def rob(arr, index):
    if index >= len(arr):
        return 0
    dp = [0 for i in range(0, len(arr))]

    for i in range(0, len(dp)):
        if dp[i] == 0:
            dp[i] = max(arr[index] + rob(arr, index+2), 0 + rob(arr, index+1))

    return dp[index]



arr = [2, 1, 1, 2]
maxele = rob(arr, 0)
print(maxele)