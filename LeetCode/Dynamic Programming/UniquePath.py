def UniquePath(m ,n):
    paths = 0

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = 1
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                dp[i][j] = dp[i][j] + ans1 + ans2

    print(dp)


m = 7
n = 3
UniquePath(m, n)