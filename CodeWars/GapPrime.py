import math
def primenumber(n1, n2):
    li = []
    # for i in range(n1, n2+1):
    #     flag = True
    #     for j in range(2, int(math.sqrt(i))+1):
    #         if i%j == 0:
    #             flag = False
    #             break
    #     if flag or i == 2:
    #         li.append(i)

    for i in range(n1, n2+1):
        flag = True
        if i <= 3:
            flag = False
        if i%2 == 0 or i%3 == 0:
            flag = False
        j=5
        while j**2 <= i:
            if i%j == 0 or i%(j+2) == 0:
                flag = False
            j += 6
        
        if flag:
            li.append(i)

    return li


def gapprime(a, start, end):
    if start == end:
        return None

    li = primenumber(start, end)
    print(li)
    for i in range(1, len(li)):
        temp = li[i] - li[i-1]
        if temp == a:
            return [li[i-1], li[i]]

    return None


answer = gapprime(10, 300, 400)
print(answer)