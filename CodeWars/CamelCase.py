def CamelCase(string):
    
    newstring = ''
    for i in range(0, len(string)):
        if i == 0:
            newstring = newstring + string[i].upper()
        elif string[i-1] == " ":
            newstring = newstring + string[i].upper()
        elif string[i] == " ":
            continue
        else:
            newstring = newstring + string[i]
        
    return newstring.strip()



string = ' hello world'
print(CamelCase(string))