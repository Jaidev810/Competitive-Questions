import sys
def MaximumSubarr(arr, n):
    
    dp = [[0 for i in range(n+1)] for j in range(0, n+1)]

    max_sum = -sys.maxsize
    for i in range(0, len(dp)):
        
        L = i + 1
        for j in range(L, len(dp[i])):
            dp[i][j] = dp[i][j-1] + arr[j-1]
            max_sum = max(max_sum, dp[i][j])
            
    print(dp)

    return max_sum
    


arr = [-2, 1]
ans = MaximumSubarr(arr, len(arr))
print(ans)