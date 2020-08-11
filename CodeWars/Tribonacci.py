def tribonacci(signature, n):
    if n == 0 :
        return []

    if n == 1:
        return signature[0]

    if n == 2:
        return [signature[0], signature[1]]

    if n == 3:
        return signature
    arr = list()
    n1, n2, n3 = signature[0], signature[1], signature[2]

    arr.append(signature[0])
    arr.append(signature[1])
    arr.append(signature[2])

    for i in range(0, n-3):
        nth = n1 + n2 + n3
        arr.append(nth)
        n1 = n2
        n2 = n3
        n3 = nth

    return arr



arr = [1, 1, 1]
n = 2
print(tribonacci(arr, n))