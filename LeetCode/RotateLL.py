class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def takeinputLL():
    print('enter the entire list')
    string = [int(x) for x in input().split()]

    head = None
    temp = None

    for curr in string:
        if curr == -1:
            break
        
        newnode = Node(curr)
        if head is None:
            head = newnode
            temp = head
        else:
            temp.next = newnode
            temp = temp.next

    return head

def first_last(head):
    temp = head
    prev = None
    while temp.next is not None:
        prev = temp
        temp = temp.next

    return prev, temp

def rotateLL(head, k):
    if head is None or head.next is None:
        return head

    temp = head
    length = 0
    while temp is not None:
        length += 1
        temp = temp.next

    k = k%length
    while k != 0:
        sec_last, last = first_last(head)
        sec_last.next = last.next
        last.next = head
        head = last
        k -= 1
    return head





def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next
    print('None')


head = takeinputLL()
new_head = rotateLL(head, 2000)
printLL(new_head)