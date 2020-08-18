import sys
def MinPathSum(arr):
    n = len(arr[0])
    m = len(arr)

    dp = [[sys.maxsize for i in range(n+1)] for j in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = arr[i][j]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                dp[i][j] = arr[i][j] + min(ans1, ans2)

    print(dp)
    return dp[0][0]





arr = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
path = MinPathSum(arr)
print(path)