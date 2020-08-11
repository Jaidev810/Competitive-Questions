arr = [10, 1, 1, 6]

li = []
flag = False
for i in range(0, len(arr)):
    price = 0
    flag = False
    if (i < len(arr) -1):
        for j in range(i+1, len(arr)):
            if (arr[i] >= arr[j]):
                price = arr[i] - arr[j]
                li.append(price)
                flag = True
                break
        if not(flag):
            li.append(arr[i])
    else:
        li.append(arr[i])

print(li)