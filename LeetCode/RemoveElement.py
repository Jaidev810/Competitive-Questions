def removeElement(arr, val):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == val:
            arr.pop(i)
            n -= 1
            i -= 1

        i += 1

    print(arr)
    return len(arr)




arr = [3, 2, 2, 3]
val = 3
length = removeElement(arr, val)
print(length)