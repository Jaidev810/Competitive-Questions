def binarySeacrh(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid +1

    return -1

def FirstandLastPosition(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end)//2
        if arr[mid] == target:
            mid2L = binarySeacrh(arr[:mid], target)
            mid2R = binarySeacrh(arr[mid+1:], target)
            if mid2L != -1:
                return mid, mid2L
            elif mid2R != -1:
                return mid, mid2R
            else:
                return mid, mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
        
    return -1

arr = [5, 7, 7, 8, 8, 10]
target = 8
print(FirstandLastPosition(arr, target))