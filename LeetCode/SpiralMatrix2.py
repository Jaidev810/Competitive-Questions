def SpiralMatrix(n):
    k = 1
    left = top = 0
    right = n -1
    bottom = n-1
    arr = []
    while True:
        temp = []
        if left > right:
            break

        for i in range(left, right+1):
            temp.append(k)
            k += 1
        left += 1

        if top > bottom:
            break

        for i in range(right, bottom+1):
            temp







n = int(input())
arr = SpiralMatrix(n)
print(arr)





