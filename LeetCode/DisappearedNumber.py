def findDisappearedNumber(arr):
    length = len(arr)

    d = dict()

    for i in range(1, length+1):
        d[i] = 0

    for i in arr:
        d[i] = d.get(i, 0) + 1

    temp = list()

    for i in d:
        if d[i] == 0:
            temp.append(i)

    return temp
    

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumber(arr))