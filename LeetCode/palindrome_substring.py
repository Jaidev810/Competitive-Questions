def check_palid(string:str) -> bool:
    test = string[::-1]
    if test == string:
        return True
    return False


def countSubString(string:str) -> int:
    temp = list()
    count = len(string)
    k = 2

    for i in range(2, len(string)+1):
        j = k
        while j < len(string)+1:
            t = string[j-i:j]
            temp.append(t)
            j += 1
        k += 1

    for x in temp:
        if check_palid(x):
            count += 1
    return count



string = input()
count = countSubString(string)
print(count)
