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

def removedupl(head):
    dic = {}
    temp = head
    while temp is not None:
        dic[temp.data] = dic.get(temp.data, 0) + 1
        temp = temp.next

    newhead = None
    temp = None

    for i in dic:
        if dic[i] == 1:
            New = Node(i)
            if newhead is None:
                newhead = New
                temp = newhead
            else:
                temp.next = New
                temp = temp.next

    return newhead


def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next

    print('None')
