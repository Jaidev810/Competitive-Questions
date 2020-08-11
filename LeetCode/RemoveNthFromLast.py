class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
def takeInput():
    inputlist = [int(x) for x in input().split()]
    head = None
    for curr in inputlist:
        if curr == -1:
            break
        Newnode = Node(curr)
        if head is None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next

    return head


def printlist(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print('None')

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next

    return count

def removenode(head, n):
    lengthLL = length(head)
    num = lengthLL - n
    if num != 0:
        prev = None
        curr = head
        for i in range(0, num):
            prev = curr
            curr =  curr.next
        prev.next = curr.next
        curr.next = None
        return head
    elif num == 0 and lengthLL > 1:
        head = head.next
        return head
    else:
        head = None
        return head
    

head = takeInput()
printlist(head)
newhead = removenode(head, 2)
printlist(newhead)    