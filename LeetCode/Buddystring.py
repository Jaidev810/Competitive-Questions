def buddystring(A, B):
    if len(A)!=len(B):
        return False
        
    not_match = [[a, b] for a, b in zip(A, B) if a!=b]
        
    if not not_match and len(set(A))<len(A): # ie. check for A and B='aa'
        return True
            
    return len(not_match)==2 and not_match[0][1]==not_match[1][0] and not_match[0][0]==not_match[1][1]



A = input()
B = input()

if buddystring(A, B):
    print('True')
else:
    print('False')




