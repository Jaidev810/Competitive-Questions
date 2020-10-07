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


def get_ele(head, n):
    prev = None
    temp = head
    while n > 1:
        prev = temp
        temp = temp.next
        n -= 1

    return prev, temp

def reverse(head):
    if head == None or head.next is None:
        return head, head
    smallhead, smalltail = reverse(head.next)
    smalltail.next = head
    head.next = None
    return smallhead, head


def reverseLL(head, m, n):
    if m >= n:
        return head
    if head is None or head.next is None:
        return head
    if m != 1:  
        prev1, cur1 = get_ele(head, m)
        prev2, cur2 = get_ele(head, n)
        temp = cur2.next
        cur2.next = None
        new_head, new_tail = reverse(cur1)
        prev1.next = new_head
        new_tail.next = temp
    else:
        prev2, cur2 = get_ele(head, n)
        temp = cur2.next
        cur2.next = None
        new_head, new_tail = reverse(head)
        new_tail.next = temp
        head = new_head
    return head


head = takeInput()
new_head = reverseLL(head, 1, 4)
printlist(new_head)