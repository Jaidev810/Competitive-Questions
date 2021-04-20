from itertools import permutations

def permutations_fun(mul:str) -> list:
    permutation = [''.join(p) for p in permutations(mul)] 
    return permutation

def all_combinations(arr:list) -> list:
    result = []

    for i in range(0, len(arr)):
        

def palindrome(number:int) -> bool:
    temp = number
    rev = 0
    while temp != 0:
        rem = temp%10
        rev = rev*10 + rem
        temp = temp//10

    if rev == number:
        return True

    return False

def numeric_palindrome(*args) -> int:
    
    mul = 1
    for val in args:
        mul = mul*val

    #all permutations of the number
    arr = permutations_fun(str(mul))

    #Combinations of each permutations
    new_arr = all_combinations(arr)

    #check if each is palindrome and if true check length
    for i range(0, len(new_arr)):
        if palindrome(new_arr[i]):
            if len(new_arr[i]) > largest:
                largest = new_arr[i]

    return largest
    
    




answer = numeric_palindrome(937, 113)
print(answer)