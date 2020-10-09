def Rotate2DArray(arr):
    
    n = len(arr[0])

    for i in range(0, n//2):
        for j in range(i, n-i-1):
            temp = arr[i][j]
            arr[i][j] = arr[n-1-j][i]
            arr[n-j-1][i] = arr[n-1-i][n-j-1]
            arr[n-i-1][n-j-1] = arr[j][n-i-1]
            arr[j][n-i-1] = temp


    return arr

    

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newarr = Rotate2DArray(arr)
print(newarr)