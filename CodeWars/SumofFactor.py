def primefactors(arr):
    p = []

    for i in range(0, len(arr)):
        factor = []

        if arr[i] > 1:
            for j in range(2, arr[i]+1):
                if arr[i]%j == 0:
                    factor.append(j)


        for j in range(0, len(factor)):
            if factor[j] > 1:
                if factor[j] == 2 and factor[j] not in p:
                    p.append(2)
                for k in range(2, factor[j]):
                    if factor[j]%k == 0:
                        break
                else:
                    if factor[j] in p:
                        continue
                    else:
                        p.append(factor[j])
    p.sort()
    return p


def Sumoffactor(arr):
    prime = primefactors(arr)
    result = []

    for i in range(0, len(prime)):
        temp = []
        num = prime[i]
        sum = 0
        for j in range(0, len(arr)):
            if arr[j]%num == 0:
                sum += arr[j]

        temp.append(num)
        temp.append(sum)
        result.append(temp)

    return result


arr = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
result = Sumoffactor(arr)
print(result)