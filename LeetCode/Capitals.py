def detectCapitalUser(word):
    if ord(word[0]) >= 65 and ord(word[0]) <= 90:
        count = 1
        for i in range(1, len(word)):
            if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                count += 1
        if count == len(word):
            return True
        if count == 1:
            return True
        else:
            return False
    elif ord(word[0]) >= 97 and ord(word[0]) <= 122:
        count = 1
        for i in range(1, len(word)):
            if ord(word[i]) >= 97 and ord(word[i]) <= 122:
                count += 1
        if count == len(word):
            return True
        else:
            return False
    else:
        return False


string = input()
print(detectCapitalUser(string))

        
