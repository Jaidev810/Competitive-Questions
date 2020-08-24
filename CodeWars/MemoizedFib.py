def recursionfib(n, dp):
    if n == 0 or n == 1:
        return n
    else:
        if dp[n-1] == -1:
            num1 = recursionfib(n-1, dp)
            dp[n-1] = num1
        else:
            num1 = dp[n-1]

        if dp[n-2] == -1:
            num2 = recursionfib(n-2, dp)
            dp[n-2] = num2
        else:
            num2 = dp[n-2]
        return num1 + num2

n = int(input())
dp = [-1 for i in range(n+1)]
ans = recursionfib(n, dp)
print(ans)