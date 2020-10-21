
def AsteroidCollision(arr):
    st = list()

    for i in range(0, len(arr)):
        # positive values in arr or first element or negative value on top
        if len(st) == 0 or st[-1] < 0 or arr[i] > 0:
            st.append(arr[i])
            continue

        else:
            while True:
                # if stack is empty
                if  len(st) == 0:
                    st.append(arr[i])
                    break
                # if top element is negative
                elif st[-1] < 0:
                    st.append(arr[i])
                    break
                # if abs value of arr is less than top
                elif -arr[i] < st[-1]:
                    break
                # if values equal
                elif -arr[i] == st[-1]:
                    del st[-1]
                    break
                # simnply delete the value 
                else:
                    del st[-1]

    return st
            

        

arr = [5, 10, -5]
new = AsteroidCollision(arr)
print(new)