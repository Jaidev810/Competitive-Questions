import sys
def MaximumProduct(nums):
    maxe = nums[0]
    mine = nums[0]
    maxp = nums[0]
        
    for i in nums[1:]:
        temp1 = i*maxe
        temp2 = i*mine
        maxe = max(i, temp1, temp2)
        mine = min(i, temp1, temp2)
        maxp = max(mine, maxe, maxp)
            
    return maxp


arr = [2, 3, -2, 4]
pro = MaximumProduct(arr)
print(pro)