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


def addLL(l1, l2):
    if l1.data == 0 and l2.data == 0 and l1.next is None and l2.next is None:
        return Node(0)
    string1 = ''
    while l1 is not None:
        string1 = string1 + str(l1.data)
        l1 = l1.next
    string2 = ''
    while l2 is not None:
        string2 = string2 + str(l2.data)
        l2 = l2.next

    sum = int(string1) + int(string2)
    print(sum)
    new_head = None
    temp = None

    while sum != 0:
        digit = sum%10
        newnode = Node(digit)
        if new_head is None:
            new_head = newnode
        else:
            newnode.next = new_head
            new_head = newnode
        sum = sum//10

    return new_head


def printLL(head):
    while head is not None:
        print(head.data, end='->')
        head = head.next

    print('None')



h1 = takeinput()
h2 = takeinput()
h3 = addLL(h1, h2)
printLL(h3)