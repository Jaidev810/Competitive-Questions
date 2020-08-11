def spiralmatrix(arr, m, n):
    top = left = 0
    bottom = m-1
    right = n-1 
    li = []
    while True:
        if left > right:
            break
        for i in range(left, right+1):
            li.append(arr[left][i])
        top += 1

        if bottom < top:
            break

        for i in range(top, bottom+1):
            li.append(arr[i][right])
        right -= 1

        if left > right:
            break
        for i in range(right, left-1, -1):
            li.append(arr[bottom][i])
        bottom -= 1

        if top > bottom:
            break
        for i in range(bottom, top-1, -1):
            li.append(arr[i][left])

        left += 1
    return li

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = len(arr)
n = len(arr[0])
li = spiralmatrix(arr, m, n)
print(li)