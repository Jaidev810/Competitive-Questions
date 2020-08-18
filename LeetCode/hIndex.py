def h_Index(arr):
    
    arr.sort()
    hindex = 0
    length = len(arr)

    for i in range(0, len(arr)):
        if hindex > length - hindex and hindex < arr[i]:
            break
        else:
            hindex += 1


    return hindex




citations = [100]
print(h_Index(citations))