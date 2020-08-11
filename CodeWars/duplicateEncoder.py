def duplicate_encode(string):
    
    d = dict()
    newstring = ''
    string = string.lower()
    for i in string:
        d[i] = d.get(i, 0) + 1

    for i in string:
        if d[i] == 1:
            newstring = newstring + '('
        else:
            newstring = newstring + ')'

    return newstring

string = input()
print(duplicate_encode(string))