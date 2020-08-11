class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def takeInput():
    inputlist = [int(x) for x in input().split()]
    head = None
    for ele in inputlist:
        if ele == -1:
            break
        Newnode = Node(ele)
        if head is None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next
    return head

def printlist(head):
    while head != None:
        print(head.data, '->', end='')
        head = head.next
    print('None')


def swapnodes(head):
    if head is None or head.next is None:
        return head
    temp = head.next
    smallhead = swapnodes(temp.next)
    h2 = head.next
    h2.next = head
    head.next  = smallhead
    return h2

head = takeInput()
printlist(head)
newhead = swapnodes(head)
printlist(newhead)


