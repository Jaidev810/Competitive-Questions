def detectpangram(string):
    
    d = dict()
    string = string.lower()
    for i in range(97, 123):
        d[chr(i)] = 0
    
    for i in string:
        d[i] = d.get(i, 0) + 1

    for i in d.values():
        if i == 0:
            return False



    return True



string = input()
if detectpangram(string):
    print('true')
else:
    print('False')