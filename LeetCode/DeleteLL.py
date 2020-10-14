class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def takeinput():
    print('enter the data:')
    inputLL = [int(x) for x in input().split()]
    head = None
    temp = None

    for cur in inputLL:
        if cur == -1:
            break
        
        newnode = Node(cur)
        if head is None:
            head = newnode
            temp = head
        else:
            temp.next = newnode
            temp = temp.next

    return head


def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next

    print('None')


def delete(head, val):
    if head is None:
        return None

    if head.data == val:
        if head.next is None:
            return None

    temp = head
    prev = None
    
    while temp is not None:
        flag = False
        if temp.data == val:
            flag = True
            if prev is None:
                temp1 = temp.next
                temp.next = None
                head = temp1
                temp = temp1
            else:
                temp1 = temp.next
                prev.next = temp.next
                temp.next = None
                temp = temp1
        if flag:
            continue
        else:
            prev = temp
            temp = temp.next

    return head


head = takeinput()
printLL(head)
new_head = delete(head, 1)
printLL(new_head)