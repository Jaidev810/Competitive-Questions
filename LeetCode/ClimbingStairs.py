def climbStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n ==2:
        return 2
    else:
        return climbStairs(n-1) + climbStairs(n-2)






n = int(input('enter the steps:'))
print(climbStairs(n))