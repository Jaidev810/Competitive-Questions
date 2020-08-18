def distributeCandies(candies, num):
    
    arr = [0 for i in range(num)]

    count = 1
    i = 0
    while candies > 0:
        if candies - count >= 0:
            if i < len(arr):
                arr[i] += count
                candies = candies - count
                count += 1
            elif i == len(arr):
                i = 0
                arr[i] += count
                candies = candies - count
                count += 1
        elif candies-count < 0 and candies > 0:
            if i == len(arr):
                i = 0
                arr[i] = arr[i] + candies
            else:
                arr[i] += candies
            candies = 0
        else:
            break

        i += 1
    
    return arr





candies = 10
num_people = 3
arr = distributeCandies(candies, num_people)
print(arr)