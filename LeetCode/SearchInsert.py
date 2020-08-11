def searchinsert(arr, tar):
    l = len(arr)
    for i in range(0, l):
        if arr[i] == tar:
            return i
    
    for i in range(0, l):
        if i < l-1:
            if arr[i] < tar and tar < arr[i+1]:
                return i+1
            elif arr[i] > tar:
                return i
        elif arr[l-1] < tar:
            return l
        else:
            return i

arr = [1]
tar = 0
print(searchinsert(arr, tar))