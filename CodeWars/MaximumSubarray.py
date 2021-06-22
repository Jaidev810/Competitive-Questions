import sys 
def maximumsubarray(arr:list):
    if len(arr) == 0:
        return 0
    max_val = -sys.maxsize
    max_end = 0
    
    for i in range(0, len(arr)):
        max_end = max_end + arr[i]
        if max_val < max_end:
            max_val = max_end
            
        if max_end < 0:
            max_end = 0
            
    return max_val




arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans = maximumsubarray(arr)
print(ans)