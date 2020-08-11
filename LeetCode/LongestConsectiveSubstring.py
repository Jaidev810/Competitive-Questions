def LongestSubstring(string):
    
    n = len(string)
    max = 0
    substring = ''

    d = dict()
    for i in string:
        d[i] = True

    count = 1
    for i in range(0, n):
        if i < n-2:
            if string[i] != string[i+1] and d[string[i]]:
                count += 1
                substring = substring + string[i]
                d[string[i]] = False
                if count > max:
                    max = count
                    newstring = substring
            else:
                substring = ''
                count = 1
        
        if count > max:
            max = count

    print(newstring)   
    return max
                
                



string = input()
length = LongestSubstring(string)
print(length)