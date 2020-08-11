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


def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head,head
    smallh, smallt = reverse(head.next)
    smallt.next = head
    head.next = None
    return smallh, head

def reverseLL(head, m, n):
    if head is None or head.next is None:
        return head
    i = 1
    temp = head
    prev = None
    while i < m:
        prev = temp
        temp = temp.next
        i += 1
    h1 = temp
    i = 1
    temp = None
    curr = head
    while i <= n and curr is not None:
        temp = curr
        curr = curr.next
        i += 1

    temp.next = None
    h2, tail = reverse(h1)
    prev.next = h2
    tail.next = curr
    return head




head = takeInput()
printlist(head)
# newhead, t = reverse(head)
# printlist(newhead)
newhead = reverseLL(head, 1, 1)
printlist(newhead)