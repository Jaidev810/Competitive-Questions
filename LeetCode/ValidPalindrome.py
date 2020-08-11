def validPalindrome(string):
    length = len(string)

    if length == 0:
        return True

    s = ''

    for i in range(0, length):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            s = s + string[i].lower()
        elif ord(string[i]) >= 97 and ord(string[i]) <= 122:
            s = s + string[i]
        elif string[i] <= str(9) and string[i] >= str(0):
            s = s + string[i]
        else:
            continue
        
    reverse = ''
    for i in range(0, len(s)):
        reverse = s[i] + reverse
    
    for i in range(0, len(s)):
        if reverse[i] != s[i]:
            return False
    
    return True


string = input()
if validPalindrome(string):
    print('true')
else:
    print('false')