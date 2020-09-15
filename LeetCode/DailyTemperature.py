def DailyTemperature(arr):
    day = list()
    for i in range(0, len(arr)):
        length = 0
        for j in range(i, len(arr)):
            if arr[j] > arr[i]:
                break
            else:
                length += 1
        else:
            length = 0
        day.append(length)


    return day
        




arr = [73, 74, 75, 71, 69, 72, 76, 73]
day = DailyTemperature(arr)
print(day)