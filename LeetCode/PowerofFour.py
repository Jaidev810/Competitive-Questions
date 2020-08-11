def isPowerofFour(num):
    
    count = 0
    if(num and not(num & (num-1))):

        while num > 1:
            num >>= 1
            count += 1
        
        if count%2 == 0:
            return True
        else:
            return False


n = int(input())
if isPowerofFour(n):
    print('true')
else:
    print('false')