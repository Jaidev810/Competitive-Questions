import sys
def UniquePath2(grid):

    m = len(grid)
    n = len(grid[0])
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[i][j] = 1
            else:
                if arr[i][j] == 1:
                    continue
                else:
                    ans1 = dp[i+1][j]
                    ans2 = dp[i][j+1]
                    dp[i][j] = arr[i][j] + ans1 + ans2
    

    return dp[0][0]



arr = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
paths = UniquePath2(arr)
print(paths)