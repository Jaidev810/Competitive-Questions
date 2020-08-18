def sortOdd(arr):
    
    for i in range(0, len(arr)-1):
        if arr[i] == 0:
            continue
        if arr[i]%2 == 0:
            continue
        else:
            index = 0
            for j in range(1, len(arr)):
                if arr[j] == 0:
                    continue
                elif arr[j]%2 == 0:
                    continue
                else:
                    if arr[j] < arr[index]:
                        arr[index], arr[j] = arr[j], arr[index]
                        index = j
        
        print(arr)

    return arr



arr = [5, 3, 2, 8, 1, 4]
print("sorted", sortOdd(arr))