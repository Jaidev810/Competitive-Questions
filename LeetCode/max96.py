num = 9669
s  = str(num)
max = num
x = num

for i in s:
    if (i == '6'):
        s = s.replace(i, '9', 1)
        if (int(s) > max):
            max = int(s)
            s = str(x)
        else:
            s = str(x)
    elif ( i == '9'):
        s =s.replace(i, '6', 1)
        if (int(s) > max):
            max = int(s)
            s = str(x)

        else:
            s = str(x)


print(max)
    