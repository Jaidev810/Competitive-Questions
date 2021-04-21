def LongestCommonPrefix(arr:list) -> str:
    if len(arr) == 0:
        return ""
    if len(arr) == 1:
        return arr[0]
    
    temp = ""

    for i in zip(*arr):
        if len(set(i)) == 1:
            temp += i[0]
        else:
            break


    return temp



arr = ["flower","flow","flight"]
prefix = LongestCommonPrefix(arr)
print(prefix)