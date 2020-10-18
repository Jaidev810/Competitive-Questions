def mergeIntervals(arr):
    new = list()
    arr.sort(key=lambda x:x[0])

    for i in range(0, len(arr)):
        if not new or new[-1][1] < arr[i][0]:
            new.append(arr[i])

        else:
            new[-1][1] = max(new[-1][1], arr[i][1])
    
    return new


arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
new = mergeIntervals(arr)
print(new)