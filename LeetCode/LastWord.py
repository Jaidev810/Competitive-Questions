string = 'b a   '
newstring = string[-1::-1]
length = 0
print(newstring)
for i in range(0, len(newstring)):
    
    if newstring[i] == ' ':
        if i == 0:
            continue
        if newstring[i-1] == ' ':
            continue
        break
    length += 1
    
print(length)