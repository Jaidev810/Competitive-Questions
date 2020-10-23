def count(n):
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count

def countBits(num):
    arr = []
    number = 0
    for i in range(0, num+1):
        bit = count(number)
        arr.append(bit)
        number += 1


    return arr




num = 5
arr = countBits(num)
print(arr)