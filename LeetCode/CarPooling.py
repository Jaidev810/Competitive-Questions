def isavaliable(trips, capacity, start):
    for i in range(0, len(trips)):
        if start == trips[i][2]:
            capacity += trips[i][0]
    return capacity

def carpool(trips, capacity):
    
    start = 1
    furthermost = 1
    for i in range(0, len(trips)):
        if furthermost < trips[i][2]:
            furthermost = trips[i][2]
    

    # main code
    while start  != furthermost + 1:
        flag = False

        for i in range(0, len(trips)):
            # pickup
            if start == trips[i][1]:
                if capacity >= trips[i][0]:
                    capacity -= trips[i][0]
                else:
                    new_capacity = isavaliable(trips[i:], capacity, start)
                    if new_capacity == capacity:
                        return False
                    else:
                        flag = True
                        capacity = new_capacity - trips[i][0]
            #drop
            if start == trips[i][2] and flag == False:
                capacity += trips[i][0]
        
        start += 1
    return True


trips = [[3,6,9],[10,2,3],[1,6,8],[2,1,6],[9,3,9]]
capacity = 12
print(carpool(trips, capacity))