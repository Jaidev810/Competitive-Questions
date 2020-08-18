import math
def RecreationOne(m, n):
    arr = []
    
    for i in range(m, n+1):
        # divisors
        temp = []
        k = 1
        div = []
        while k <= math.sqrt(i):
            if i%k == 0:
                if i//k == k:
                    div.append(k)
                else:
                    div.append(k)
                    div.append(i//k)
            k += 1
        #sqaure of divisors
        sum = 0
        k = 0
        while k < len(div):
            sum = sum + div[k]*div[k]
            k += 1

        num = math.sqrt(sum) 

        if num - math.floor(num) == 0:
            temp.append(i)
            temp.append(sum)
            arr.append(temp)

    return arr



m = int(input())
n = int(input())
print(RecreationOne(m, n))