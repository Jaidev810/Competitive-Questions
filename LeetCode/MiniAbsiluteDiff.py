arr = [4, 2, 1, 3]

list.sort(arr)

li = []

for i in range(0, len(arr)):
    diff = 2147483648
    for j in (i, len(arr) -1):
        index_diff = arr[i] - arr[j]

        if (diff > index_diff):
            diff = index_diff

print(diff)