def arr_diff(arr1, arr2):
    
    if len(arr2) == 0:
        return arr1

    result = list()
    for i in range(0, len(arr1)):
        flag = False
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                flag = True
        if not flag:
            result.append(arr1[i])

    return result 



arr1 = [1, 2, 2, 2, 3 ]
arr2 = [2]
print(arr_diff(arr1, arr2))