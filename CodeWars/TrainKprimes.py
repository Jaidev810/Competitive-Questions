import math
def primefactors(num):
    li = []
    while num%2 == 0:
        li.append(2)
        num = num//2

    for i in range(3, int(math.sqrt(num))+1):
        while num%i == 0:
            li.append(i)
            num = num//i

    if num > 2:
        li.append(num)
    return li

def kPrimes(k, m, n):
    if m == 0:
        m += 1
    arr = []
    for i in range(m, n+1):
        li = primefactors(i)
        if len(li) == k:
            arr.append(i)

    return arr

def puzzle(sum):
    a = kPrimes(1, 0, sum)
    b = kPrimes(3, 0, sum)
    c = kPrimes(7, 0, sum)
    count = 0
    for i in a:
        for j in b:
            for k in c:
                if i + j + k == sum:
                    count += 1
    return count
        


arr = kPrimes(5, 500, 600)
ans = puzzle(138)
print(arr)
print(ans)