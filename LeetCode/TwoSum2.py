def Twosum(arr, target):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            return [i+1, j+1]
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]




arr= [2, 3, 4]
target = 6

new = Twosum(arr, target)
print(new)