def search2Dmatrix(arr, target):
    m = len(arr)
    n = len(arr[0])
    row = -1
    for i in range(0, m):
        if arr[i][0] <= target and arr[i][n-1] >= target:
            row = i
            break
    if row == -1:
        return False

    for i in range(0, len(arr[row])):
        if arr[row][i] == target:
            return True
        
    return False





arr = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
flag = search2Dmatrix(arr, target)
print(flag)