def common(arr:list) -> list:
    li = list(arr[0])
    
    for i in arr:
        temp = []
        for j in i:
            if j in li:
                temp.append(j)
                li.remove(j)
        li = temp


    return li





li = ['cool', 'lock', 'cook']
common_ele = common(li)
print(common_ele)
