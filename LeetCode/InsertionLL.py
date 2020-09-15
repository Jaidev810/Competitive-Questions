class LinkedList:
    def __init__(self, data, next='None'):
        self.data = data
        self.next = next


def takeinputLL():
    inputlist = [int(x) for x in input().split()]
    head = None
    temp = None

    for cur in inputlist:
        if cur == -1:
            break

        Newnode = LinkedList(cur)
        if head is None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next

    return head


def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next

    print('None')


def insertionLL(head):
    
    test = LinkedList(0, head)
    curr = head
    
    while curr.next is not None:
        if curr.next.data >= curr.data:
            curr = curr.next

        else:
            temp = curr.next
            temp1 = test
            curr.next = curr.next.next

            while temp1.next.data <= temp.data:
                temp1 = temp1.next
            temp1.next, temp.next = temp, temp1.next

    return test.next


head = takeinputLL()
printLL(insertionLL(head))