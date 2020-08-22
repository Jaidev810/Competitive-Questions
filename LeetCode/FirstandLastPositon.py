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
    ind1, ind1 = -1, -1

    for i in range(0, len(arr)):
        if arr[i] == target:
            ind1 = i
            break

    for i in range(ind1, len(arr)):
        if arr[i] == target:
            ind2 = i

    return ind1, ind2

arr = [5, 7, 7, 8, 8, 8, 8, 10]
target = 8
print(FirstandLastPosition(arr, target))