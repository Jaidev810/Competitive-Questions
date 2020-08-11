arr = ['cool', 'lock', 'cook']

li = []
freq = [0]*256

flag = False

for i in range(0, len(arr)):
    for j in range(0, len(arr[i])):
        char = ord(arr[i][j])
        freq[char] = freq[char] + 1

for i in range(0, len(freq)):
    if ( freq[i] > 0):
        if(freq[i] == len(arr)):
            li.append(chr(i))
        elif (freq[i]%len(arr) == 0 or freq[i] > len(arr)):
            temp = freq[i]//len(arr)
            j = temp
            while j > 0:
                li.append(chr(i))
                j -=1

print(li)
