def Merge(s1, s2, arr):
    i, j, k = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            arr[k] = s1[i]
            i += 1
            k += 1
        else:
            arr[k] = s2[j]
            j += 1
            k += 1
    while i < len(s1):
        arr[k] = s1[i]
        i += 1
        k += 1
    while j < len(s2):
        arr[k] = s2[j]
        j += 1
        k += 1


def MergeSort(arr):
    length = len(arr)
    if length == 0 or length == 1:
        return arr
    mid = length//2
    s1 = arr[0:mid]
    s2 = arr[mid:]
    MergeSort(s1)
    MergeSort(s2)
    Merge(s1, s2, arr)


def removeduplicate(a, x):
    index = 1
    if len(a)==0:
        return 0
    previous = x
    for i in range(0,len(a)):
        if previous!=a[i]:
            a[index], a[i] = a[i], a[index]
            index+=1
    return index, arr




arr = [3, 2, 2, 3]
x = 3
arr = removeduplicate(arr,x)
print(arr)
