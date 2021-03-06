def intersection(arr1, arr2):
    i = 0
    j = 0
    arr1.sort()
    arr2.sort()

    unique = set()

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            unique.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1
    return list(unique)



arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
ele = intersection(arr1, arr2)
print(ele)