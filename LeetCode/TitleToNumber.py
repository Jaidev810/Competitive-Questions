def titleToNumber(string):
    length = len(string)

    if length == 1:
        return ord(string[0]) - 64

    i = 0
    sum = 0
    number = 0
    k = length -1
    while i < length:
        number = (26**i)*(ord(string[k]) - 64)
        sum = sum + number
        i += 1
        k -= 1

    return sum
    


string = input()
print(titleToNumber(string))