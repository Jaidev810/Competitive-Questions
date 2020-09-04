def RepeatingSubstring(string):
    length = len(string)

    if length == 1:
        return False

    i = 1
    while i < length:
        if length%i == 0:
            if string == string[:i]*(length//i):
                return True
        i += 1
    return False


string = input()
if RepeatingSubstring(string):
    print('True')
else:
    print('False')