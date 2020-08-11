class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
def takeinputLL():
    print('enter the linked list:')
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


def printLL(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next

    print('None')

def middleLL(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


head = takeinputLL()
printLL(head)
print(middleLL(head).data)

