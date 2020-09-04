def SumofPairs(arr, sum):
    if len(arr) == 0:
        if sum == 0:
            return ['']
        else:
            return []


    num = arr[0]
    output = list()

    li1 = SumofPairs(arr[1:], sum-num)
    for i in range(0, len(li1)):
        newstring = str(num) + ' ' + li1[i]
        li1[i] = newstring

    li2 = SumofPairs(arr[1:], sum)

    for i in range(0, len(li1)):
        output.append(li1[i])

    for i in range(0, len(li2)):
        output.append(li2[i])

    return output


arr = [1, 4, 8, 7, 3, 15]
ans = SumofPairs(arr, 8)
print(ans)
