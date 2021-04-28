def PlusOne(arr:list) -> list:
    string = ''
    for x in arr:
        string = string + str(x)
    number = int(string) + 1
    new_arr = []
    for x in str(number):
        new_arr.append(int(x))
    return new_arr





arr = [0]
new_arr = PlusOne(arr)
print(new_arr)