import sys
def closetsum(arr, target):
    diff = sys.maxsize
    arr.sort()
    
    i = 0
    length = len(arr)

    while i < length:
        j = i+1
        k = length-1

        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if abs(diff) > abs(target-sum):
                diff = target-sum
            if sum < target:
                j += 1
            else:
                k -= 1
        if diff == 0:
            break

        i += 1
    
    return target-diff


                



arr = [-1, 2, 1, -4]
target = 1
close = closetsum(arr, target)
print(close)