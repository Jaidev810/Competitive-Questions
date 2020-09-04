def search2d(arr, target):

    for i in range(0, len(arr)):
        startc = 0
        endc = len(arr[i])-1

        while startc <= endc:
            midc = (startc+endc)//2
            if arr[i][midc] == target:
                return True
            elif arr[i][midc] > target:
                endc = midc -1
            else:
                startc = midc + 1

    return False

arr = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 20
if search2d(arr, target):
    print('true')
else:
    print('false')