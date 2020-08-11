def AddDigit(num):

    digit = 0

    while True:
        while num != 0:
            rev = num%10
            digit = digit + rev
            num = num//10

        if digit//10 == 0:
            break
        else:
            num = digit
            digit = 0

    return digit



num = int(input())
digit = AddDigit(num)
print(digit)