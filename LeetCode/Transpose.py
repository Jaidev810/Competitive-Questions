arr = [[1, 2, 3], [4, 5, 6]]
n = len(arr)
m = len(arr[0])

li = []

for i in range(0, m):
    temp = []
    for j in range(0, n):
        temp.append(arr[j][i])

    li.append(temp)

print(li)