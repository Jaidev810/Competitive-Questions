import math

def PowerofThree(n:int) -> bool:
    if n < 1:
        return False

    answer = math.log(n, 3)
    flag = abs(answer - round(answer)) < 1e-10
    return flag




number = int(input())
if PowerofThree(number):
    print("True")
else:
    print("False")