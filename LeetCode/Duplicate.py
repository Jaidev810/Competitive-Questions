def duplicate(arr):
    arr.sort()
    for i in range(0, len(arr)):
        if i < len(arr) - 1:
            if arr[i] == arr[i+1]:
                return arr[i]
        else:
            return None   





arr = [3, 1, 3, 4, 2]
dup = duplicate(arr)
print(dup)