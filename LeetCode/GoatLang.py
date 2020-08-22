def GoatLang(string):
    

    string = string.split()
    j = 1


    for i in range(0, len(string)):
        if ord(string[i][0].lower()) == 65 or ord(string[i][0].lower()) == 101 or ord(string[i][0].lower()) == 105 or ord(string[i][0]) == 111 or ord(string[i][0]) == 117:
            string[i] = string[i] + 'ma'
        else:
            string[i] = string[i] + string[i][0]
            string[i] = string[i][1:]
            string[i] = string[i] + 'ma'
        
        temp = j
        while temp > 0:
            string[i] = string[i] + 'a'
            temp -= 1
        j += 1
    
    newstring = ''
    for i in string:
        newstring = newstring + i + ' '

    for i in range(0, len(newstring)-1):
        newstring = newstring
    return newstring
        





string = input()
newstring = GoatLang(string)
print(newstring)