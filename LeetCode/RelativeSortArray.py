arr1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23 ,29, 48, 30, 31]
arr2 = [2, 42, 38, 0, 43, 21]

li = []

list.sort(arr1)

for i in range(0, len(arr2)):
    temp = arr2[i]
    for j in range(0, len(arr1)):
        if (temp == arr1[j]):
            li.append(temp)

for i in range(0, len(arr1)):
    count = 0
    for j in range(0, len(arr2)):
        if (arr1[i] == arr2[j]):
            count +=1
    
    if(count == 0):
        li.append(arr1[i])
print(li)
