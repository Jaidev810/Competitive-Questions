s = 'RLRRLLRLRL'


countl = 0

ans = 0

for i in range(0, len(s)):
    if (s[i] == 'L'):
        countl +=1

    else:
        countl -=1
    if (countl == 0):
        ans +=1
print(ans)