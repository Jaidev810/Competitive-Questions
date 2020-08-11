def Triplet(arr, n):
    arr.sort()
    li = []
    for i in range(0, n - 1):  
          
        # initialize left and right 
        l = i + 1; 
        r = n - 1; 
        x = arr[i]; 
        while (l < r) : 
            if (x + arr[l] + arr[r] == 0) : 
                  
                # print elements if it's sum  
                # is given sum. 
                temp= []
                temp.append(x)
                temp.append(arr[l])
                temp.append(arr[r])
                li.append(temp)
                l = l + 1; 
                r = r - 1; 
              
            # If sum of three elements is less 
            # than 'sum' then increment in left 
            elif (x + arr[l] + arr[r] < 0): 
                l = l + 1; 
  
            # if sum is greater than given sum,  
            # then decrement in right side 
            else: 
                r = r - 1; 
    return li

arr = [-1, 0, 1, 2, -1, -4]
newarr = Triplet(arr, len(arr))
print(newarr)
