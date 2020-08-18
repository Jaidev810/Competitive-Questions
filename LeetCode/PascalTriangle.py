def PascalTriangle(rowIndex):
    arr = list()
    temp = list()
    temp.append(1)
    arr.append(temp)
    temp = []
    temp.append(1)
    temp.append(1)
    arr.append(temp)
    sample = list()
    i = 3

    while i <= rowIndex+1:
        j = 0
        sample = list()
        while j < len(temp):
            sample.append(temp[j])
            j += 1

        print('sample:', sample)
        temp = []
        temp = [1 for j in range(0, i)]
        k = 1

        times = len(sample) - 1
        while times > 0:
            prev1 = sample.pop(0)
            prev2 = sample.pop(0)
            sample.insert(0, prev2)
            temp[k] = prev1 + prev2
            k += 1
            times -= 1

        arr.append(temp)
        print('temp', temp)
        i += 1


    return arr[rowIndex]







rowIndex = int(input())
print(PascalTriangle(rowIndex))