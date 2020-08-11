def maskify(string):
    length = len(string)
    if length <= 4:
        return string

    newstring = ''
    for i in range(0, length-4):
        newstring = newstring + '#'

    for i in range(length-4, length):
        newstring = newstring + string[i]

    return newstring

string = input()
print(maskify(string))