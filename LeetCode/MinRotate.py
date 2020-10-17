def minrotate(arr):
    i = 0
    j = len(arr)-1

    while i < j :
        mid = (i+j)//2
        if arr[mid] < arr[mid-1]:
            return arr[mid]
        if arr[mid+1] < arr[mid]:
            return arr[mid+1]
        elif arr[mid] > arr[0]:
            i = mid+1
        else:
            j = mid-1

    return arr[0]




arr = [4, 5, 6, 7, 0, 1, 2, 3]
element = minrotate(arr)
print(element)