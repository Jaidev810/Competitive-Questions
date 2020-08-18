def SpiralMatrix(n):
    temp = [[0 for i in range(n)] for j in range(n)]

    k = 1
    top, left = 0, 0
    bottom = n - 1
    right = n -1

    while True:

        if left > right:
            break

        for i in range(left, right+1):
            temp[left][i] = k
            k += 1
        top += 1

        if top > bottom:
            break

        for i in range(top, bottom+1):
            temp[i][right] = k
            k += 1
        right -=1

        if left > right:
            break

        for i in range(right, left-1, -1):
            temp[bottom][i] = k
            k += 1
        bottom -= 1

        if top > bottom:
            break
        for i in range(bottom, top-1, -1):
            temp[i][left] = k
            k += 1
        left += 1            

    return temp


n = int(input())
arr = SpiralMatrix(n)
print(arr)





