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
        NewNode = Node(curr)
        if head is None:
            head = NewNode
            temp = head
        else:
            temp.next = NewNode
            temp = temp.next
    return head

def printlist(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print('None')

def midpoint(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(s1, s2):
    if s1 is None and s2 is not None:
        return s2
    if s2 is None and s1 is not None:
        return s1
    
    if s1.data < s2.data:
        finalh = s1
        finalt = s1
        s1 = s1.next
    else:
        finalh = s2
        finalt = s2
        s2 = s2.next

    while s1 is not None and s2 is not None:
        if s2.data < s1.data:
            finalt.next = s2
            finalt = s2
            s2 = s2.next
        else:
            finalt.next = s1
            finalt = s1
            s1 = s1.next
    while s1 is not None:
        finalt.next = s1
        finalt = s1
        s1 = s1.next
    while s2 is not None:
        finalt.next = s2
        finalt = s2
        s2 = s2.next
    return finalh

def MergeSort(head):
    if head is None or head.next is None:
        return head

    middle = midpoint(head)
    head2 = middle.next
    middle.next = None
    h1 = MergeSort(head)
    h2 = MergeSort(head2)
    finalh = merge(h1, h2)
    return finalh


head = takeInput()
printlist(head)
newhead = MergeSort(head)
printlist(newhead)