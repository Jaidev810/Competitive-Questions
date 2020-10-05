class LL:

    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    print('enter the head:')
    inputlist = [int(x) for x in input().split()]

    head = None
    temp = None

    for curr in inputlist:
        if curr == -1:
            break

        Newnode = LL(curr)
        if head is None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next
        
    return head



def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next
    print('None')

def length(head):
    count  = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def intersectionLL(headA, headB):
    c1 = length(headA)
    c2 = length(headB)
        
    if c1 < c2:                    
        for _ in range(c2 - c1):
            headB = headB.next
    else:
        for _ in range(c1 - c2):
            headA = headA.next            
        
    while headA is not headB:
        headA = headA.next
        headB = headB.next                
        
    return headA


head1 = takeInput()
head2 = takeInput()
ans = intersectionLL(head1, head2)
print(ans)