def setmatrixzero(arr):
    m = len(arr)
    n = len(arr[0])
    zero = []
    for i in range(0, m):
        for j in range(0, n):
            if arr[i][j] == 0:
                temp = []
                temp.append(i)
                temp.append(j)
                zero.append(temp)
                continue

    while len(zero) != 0:
        li = zero.pop(0)
        print(li)
        row = li[0]
        column = li[1]
        for i in range(0, m):
            arr[i][column] = 0
        for i in range(0, n):
            arr[row][i] = 0
    



arr =[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setmatrixzero(arr)
print(arr)