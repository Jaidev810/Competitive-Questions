def hasAllCodes(string:str, k:int) -> bool:
    temp = set()
    count = 1 << k
    for i in range(k, len(string)+1):
        a = string[i-k:i]
        if a not in temp:
            temp.add(a)
            count -= 1
            if count == 0:
                return True
    return False





string = input()
k = int(input())
if hasAllCodes(string, k):
    print("true")
else:
    print("false")