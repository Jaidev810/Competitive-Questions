class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def takeinput():
    inputlist = [int(x) for x in input().split()]
    head = None
    temp = head
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

def printLL(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print('None')

def lengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def reverse(head):
    if head is None:
        return
    if head.next is None:
        return head
    smallh, smallt = reverse(head)
    smallt.next = head
    head.next = None
    return smallh, head



def palindrome(head):
    if head is None:
        return 
    size = lengthLL(head)
    if size%2 == 0:
        mid = size//2
    else:
        mid = size//2 + 1
    h1 = head
    i = 0
    while i < mid:
        h1 = h1.next
        i += 1
    h2 = h1
    h2, tail = reverse(h2)
    while h2 is not None:
        if head.data != h2.data:
            return False
        head = head.next
        h2 = h2.next

    return True


head = takeinput()
printLL(head)
if palindrome:
    print('true')
else:
    print('false')
    