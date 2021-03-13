import sys

def sortOdd(arr):
    
    # for i in range(0, len(arr)-1):
    #     if arr[i] == 0:
    #         continue
    #     if arr[i]%2 == 0:
    #         continue
    #     else:
    #         index = 0
    #         for j in range(1, len(arr)):
    #             if arr[j] == 0:
    #                 continue
    #             elif arr[j]%2 == 0:
    #                 continue
    #             else:
    #                 if arr[j] < arr[index]:
    #                     arr[index], arr[j] = arr[j], arr[index]
    #                     index = j
        
    #     print(arr)
    testing = []

    for i in range(0, len(arr)):
        if arr[i]%2 == 0:
            testing.append(arr[i])
        else:
            testing.append(-sys.maxsize)

    arr.sort()
    j = 0
    i = 0

    while j < len(testing) and i < len(arr):
        if testing[j] == -sys.maxsize and arr[i]%2 != 0:
            testing[j] = arr[i]
            i += 1
            j += 1
        
        elif arr[i]%2 == 0 and testing[j] == -sys.maxsize:
            i += 1

        elif testing[j] != -sys.maxsize and arr[i]%2 != 0:
            j += 1
        else:
            i += 1
            j += 1

    print(testing)
    print(arr)
    print()
 
    return testing



arr = [5, 3, 1, 8, 0]
print("sorted", sortOdd(arr))