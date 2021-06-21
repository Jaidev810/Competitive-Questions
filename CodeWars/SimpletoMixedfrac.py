## without the use of fractions library


import math
def fraction(s:str):
    flag = False
    num1, num2 = s.split('/')

    if num2 == '0':
        raise ZeroDivisionError
    if num1 == '0':
        return '0'
        
    if num1[0] == '-' and num2[0] != '-':
        num1 = int(num1[1:])
        flag = True
    
    elif num1[0] == '-' and num2[0] == '-':
        num1 = num1[1:]
        num2 = num2[1:]
        
    elif num1[0] != '-' and num2[0] == '-':
        flag = True
        num2 = num2[1:]
        
    num2 = int(num2)
    num1 = int(num1)
    
    num1, num2 = cleaner(num1, num2)
    
    if num2 != 1:
        temp1 = num1//num2
        temp2 = num1 - temp1*num2
        if temp1 == 0 and not flag:
            return str(temp2) + '/' + str(num2)
        if temp1 == 0 and flag:
            return "-" + str(temp2) + '/' + str(num2)
        if flag:
            return "-" + str(temp1) + " " + str(temp2) + "/" + str(num2)
        else:
            return str(temp1) + " " + str(temp2) + "/" + str(num2)
    else:
        if flag:
            return "-" + str(num1)
        return str(num1)
    
def primefactors(n):
    li = list()
    while n%2 == 0:
        li.append(2)
        n = n//2
    for i in range(3, int(math.sqrt(n))+1):
        while n%i == 0:
            li.append(i)
            n = n//i
    if n>2:
        li.append(n)
    return li
    
    
def cleaner(num1, num2):
    li1 = primefactors(num1)
    li2 = primefactors(num2)
    i = 0
    while i < len(li1):
        if li1[i] in li2:
            li2.remove(li1[i])
            li1.remove(li1[i])
            i -= 1
        i += 1
            
    if len(li1) != 0  and len(li2) != 0:
        temp = 1
        for i in li1:
            temp = temp*i
        temp2 = 1
        for i in li2:
            temp2 = temp2*i
        return temp, temp2
    if len(li2) == 0:
        temp1 = 1
        for i in li1:
            temp1 = temp1*i
        return temp1, 1
    


# string = "-1317115/7806182"
string = '418098/-5601478'
ans = fraction(string)
print(ans)