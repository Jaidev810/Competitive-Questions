def buildTower(number):
    i = 1
    arr = list()

    while i <= number:
        newstring = ''
        gaps = number-i
        while gaps > 0:
            newstring = newstring + ' '
            gaps -= 1
        
        for j in range(0, i):
            newstring = newstring + '*'

        k = 2
        while k <= i:
            newstring = newstring + '*'
            k += 1

        gaps = i
        while gaps < number:
            newstring = newstring + ' '
            gaps += 1

        arr.append(newstring)
        i += 1

    return arr



number = int(input())
print(buildTower(number))