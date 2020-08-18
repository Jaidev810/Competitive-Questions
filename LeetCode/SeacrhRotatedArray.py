def binarySearchN(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binarySearchD(arr, target, index):
    start = 0
    end = len(arr) - 1
    lastele = arr[end]
    mid = index
    while start <= end:

        if arr[mid] == target:
            return mid
        elif arr[mid] < target and lastele < target:
            end = mid - 1
            lastele = arr[end]
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        mid = (start+end)//2

    return -1 



def SearchRotatedArray(nums, target):
    if len(nums) == 0:
        return -1
    
    length = 0
    temp = nums[0]

    for i in range(0, len(nums)):
        if temp <= nums[i]:
            length += 1
        else:
            break
    
    if length == len(nums):
        return binarySearchN(nums, target)
    else:
        return binarySearchD(nums, target, length)


nums = []
target = 5
index = SearchRotatedArray(nums, target)
print(index)