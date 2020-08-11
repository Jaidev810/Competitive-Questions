arr = ['cat', 'bt', 'hat', 'tree']

char = 'atach'
temp = 0
li = []

freq2 = [0]*256

for i in range(0, len(char)):
    c = ord(char[i])
    freq2[c] = freq2[c] + 1



for i in range(0, len(arr)):
    s = arr[i]
    freq1 = [0]*256
    for j in range(0, len(s)):
        c = ord(s[j])
        freq1[c] = freq1[c] + 1

    temp = ''
    for m in range(0, len(s)):
        c = ord(s[m])
        if (freq1[c] <= freq2[c]):
            temp = temp + chr(c)

    if (temp == arr[i]):
        li.append(i)
    
print(li)
