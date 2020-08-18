def alphabet_number(text):
    
    newstring = ''
    for i in range(0, len(text)):
        if ord(text[i]) >= 65 and ord(text[i]) <= 90:
            newstring = newstring + str(ord(text[i]) - 64) + ' '
        elif ord(text[i]) >= 97 and ord(text[i]) <= 122:
            newstring = newstring + str(ord(text[i]) - 96) + ' '
        else:
            continue
    return newstring[:len(newstring)]


text = input()
print(alphabet_number(text))