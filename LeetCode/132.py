import sys

def pattern(arr):
    # O(n^3)
    # for i in range(0, len(arr)):
    #     for j in range(i+1, len(arr)):
    #         for k in range(j+1, len(arr)):
    #             if arr[i] < arr[k] and arr[k] < arr[j]:
    #                 return True
    min_i = sys.maxsize
    for i in range(0, len(arr)-1):
        min_i = min(min_i, arr[i])
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and min_i < arr[j]:
                return True
    return False

arr = [-2, 1, 2, -2, 1, 2]
flag = pattern(arr)
if flag:
    print('True')
else:
    print('False')