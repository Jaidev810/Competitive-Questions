def ValidParenthesis(string):
    
    stack = []
    flag = True
    for i in range(0, len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            if len(stack) == 0:
                stack.append(string[i])
            else:
                temp = stack.pop()
                if temp == '(':
                    flag = True
                else:
                    flag = False
    if len(stack) == 0:
        return flag
    else:
        return flag
    


string = input()
if ValidParenthesis(string):
    print('true')
else:
    print('false')