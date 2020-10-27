class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def takeinput():
    print('enter the list data: ')
    inputlist = [int(x) for x in input().split()]
    head = None
    temp = None

    for i in inputlist:
        if i == -1:
            break
        newnode = Node(i)
        if head is None:
            head = newnode
            temp = head
        else:
            temp.next = newnode
            temp = temp.next

    return head


def linkedcycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow



def printll(head):
    while head:
        print(head.data, end='->')
        head = head.next

    print('None')

head = takeinput()
printll(head)