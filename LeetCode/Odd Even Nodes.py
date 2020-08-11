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
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print('None')


def OddEvenNode(head):
    if head is None:
        return None
    evenh = None
    event = None
    oddh = None
    oddt = None
    i = 1
    while head is not None:
        if i%2 == 0:
            if evenh is None:
                evenh = head
                event = head
            else:
                event.next = head
                event = event.next
        else:
            if oddh is None:
                oddh = head
                oddt = head
            else:
                oddt.next = head
                oddt = oddt.next
        head = head.next
        i += 1

    if oddh is not None and evenh is not None:
        oddt.next = evenh
        event.next = None
        return oddh
    elif oddh is not None and evenh is None:
        oddt.next = None
        return oddh
    event.next = None
    return evenh


head = takeInput()
printlist(head)
newLL = OddEvenNode(head)
printlist(newLL)