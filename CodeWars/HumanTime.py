def HumanTime(seconds):
    
    ss = ''
    mm = ''
    hh = ''

    ##seconds
    sec = seconds//60
    sec1 = seconds - sec*60
    digit = sec1
    count = 0
    while digit != 0:
        temp = digit%10
        count += 1
        digit = digit//10
    
    if count == 1 or sec1 == 0:
        ss = '0'
    ss = ss + str(sec1)

    ##minutes
    min1 = sec//60
    min2 = sec - min1*60
    digit = min2
    count = 0
    while digit != 0:
        temp = digit%10
        count += 1
        digit = digit//10

    if count == 1 or min2 == 0:
        mm = '0'
    mm = mm + str(min2)


    ##hr
    digit = min1
    count = 0
    while digit != 0:
        temp = digit%10
        count += 1
        digit = digit//10
    if count == 1 or min1 == 0:
        hh = '0'
    hh = hh + str(min1)

    return hh + ':' + mm + ':' + ss


seconds = int(input())
string = HumanTime(seconds)
print(string)