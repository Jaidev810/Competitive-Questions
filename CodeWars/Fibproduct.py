def fibproduct(pro):
    dp = [0 for i in range(500)]

    arr = []
    dp[0] = 0
    dp[1] = 1

    for i in range(2, 500):
        dp[i] = dp[i-1] + dp[i-2]
        product = dp[i-1]*dp[i-2]
        if product == pro:
            arr.append(dp[i-1])
            arr.append(dp[i-2])
            arr.append("True")
            print(i)
            break
        elif product > pro:
            arr.append(dp[i-1])
            arr.append(dp[i-2])
            arr.append("False")
            print(i)
            break

    return arr




n = int(input())
arr = fibproduct(n)
print(arr)