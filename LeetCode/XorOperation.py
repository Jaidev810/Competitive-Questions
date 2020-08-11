n = 5
start = 0

nums = [] 
for i in range(0, n):
    temp = start + 2*i
    nums.append(temp)

for i in range(0, len(nums)):
    if (i==0):
        ans = nums[i]
    else:
        ans = ans^nums[i]
    

print(ans)