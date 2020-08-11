def moveZero(arr):
    length = len(arr)

    i = 0
    k = 0

    while k < length:
        if arr[i] == 0:
            temp = arr.pop(i)
            arr.append(temp)
            i -= 1

        i += 1
        k += 1


arr = [0, 1, 0, 3, 12, 0]
moveZero(arr)
print(arr)