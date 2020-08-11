def findAllDuplicates(nums):
    d = dict()
    for i in nums:
        d[i] = d.get(i, 0) + 1

    dup = list()
    print(d)

    for i in d:
        if d[i] == 2:
            dup.append(i)

    return dup


nums = [4, 3, 2, 7, 8, 2, 3, 1]
dup = findAllDuplicates(nums)
print(dup) 