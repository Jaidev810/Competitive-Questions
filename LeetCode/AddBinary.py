def binarytoDecimal(a:str) -> int:
    dec = 0
    i = 0
    n = int(a)
    while n!= 0:
        rem = n%10
        n = n//10
        dec += rem*(2**i)
        i += 1
    return dec


def AddBinary(a:str, b:str) -> str:
    num1 = binarytoDecimal(a)
    num2 = binarytoDecimal(b)

    # decimal to binary
    temp = num1 + num2
    place = 1
    binary = 0

    while temp > 0:
        rem = temp%2
        binary += rem*place
        place *= 10
        temp = temp//2

    return str(binary)


a = '1010'
b = '1011'
number = AddBinary(a, b)
print(number)