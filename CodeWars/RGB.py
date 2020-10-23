def gethexa(num):
    if num <= 0:
        return '00'
    elif num >= 255:
        return 'FF'
    else:
        if num >= 0 and num <= 9:
            return '0' + str(num)
        else:
            rem = num%16
            quo = num//16
            if rem > 9 and quo > 9:
                alp1 = 65 + rem -10
                alp2 = 65 + quo -10
                return chr(alp2) + chr(alp1)
            elif rem > 9:
                alp1 = 65 + rem-10
                return str(quo) + chr(alp1)
            elif quo > 9:
                alp1 = 65 + quo -10
                return chr(alp1) + str(rem)
            else:
                return str(quo) + str(rem)


def rgb(r, g, b):
    hexa_r = gethexa(r)
    hexa_g = gethexa(g)
    hexa_b = gethexa(b)
    return hexa_r + hexa_g + hexa_b



r = 254
g = 253
b = 252

string = rgb(r, g, b)
print(string)