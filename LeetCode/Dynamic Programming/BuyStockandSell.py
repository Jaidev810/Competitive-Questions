def BuySellStock2(arr, n):
    dp = [-10 for i in range(n+1)]

    dp[n] = arr[n-1]
    maxprofit = -10000000000

    sell = arr[n-1]

    for k in range(n-1, 0, -1):
        sell = max(arr[k-1], sell)
        buy = arr[k-1]
        print(sell, ' ', buy)
        profit = sell - buy

        dp[k] = profit
        maxprofit = max(profit, maxprofit)
    print(dp)
        
    return maxprofit



arr = [7, 1, 5, 3, 6, 4]
print(BuySellStock2(arr, 5))