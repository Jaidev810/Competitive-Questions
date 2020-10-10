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

def createLL(arr):
    new_arr = list(dict.fromkeys(arr))

    head = None
    temp = None

    for i in new_arr:
        newnode = Node(i)
        if head is None:
            head = newnode
            temp = head
        else:
            temp.next = newnode
            temp = temp.next

    return head

def removeduplicate(head):
    if head is None or head.next is None:
        return head

    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    
    new_head = createLL(arr)
    return new_head

def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next

    print('None')


head = takeinput()
new_head = removeduplicate(head)
printLL(new_head)

