s = 'loveleetcode'
c = 'e'

arr = []


for i in range(0, len(s)):
    count = 0
    char = s[i]
    for j in range(i, len(s)):
        if(s[j] != c):
            count += 1
        else:
            arr.append(count)
            break

print(arr)