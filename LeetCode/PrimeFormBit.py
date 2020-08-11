
l = 10
r = 15
ans = 0
while l <= r:
    result = 0
    temp = l
    while (temp):
        result += temp & 1
        temp >>= 1

    flag = True
    i = 2
    while i < result:
        if (result%i==0):
            flag = False
        i +=1

    if (flag and result > 1):
        ans += 1

    l +=1

print(ans)