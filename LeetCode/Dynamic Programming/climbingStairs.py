def climbingStairs(n):
    if n == 1:
        return 1
    
    dp = [-1 for i in range(n+1)]

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        num1 = dp[i-2]
        num2 = dp[i-1]
        dp[i] = num1 + num2

    return dp[n]



n = int(input())
steps = climbingStairs(n)
print(steps)