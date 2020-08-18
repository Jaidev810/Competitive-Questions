def createPhoneNumber(arr):
    newstring = '('

    for i in range(0, 3):
        newstring = newstring + str(arr[i])
    
    newstring = newstring + ') '

    for i in range(3, 6):
        newstring = newstring + str(arr[i])

    newstring = newstring + '-'

    for i in range(6, len(arr)):
        newstring = newstring + str(arr[i])

    return newstring


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(createPhoneNumber(arr))