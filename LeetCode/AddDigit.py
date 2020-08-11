class Node:

    def __init__(self , data):
        self.data = data
        self.next = None

def takeInput():
    inputlist = [int(x) for x in input().split()]
    head = None
    temp = None
    for curr in inputlist:
        if curr == -1:
            break
        Newnode = Node(curr)
        if head == None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next
    return head

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def numberlist(head):
    temp = ''
    while head is not None:
        temp = str(head.data) + temp
        head = head.next
    return temp

def printlist(head):
    while head is not None:
        print(head.data, '->', end='')
        head = head.next
    print('None')

def newll(result):
    head = None
    while result is not 0:
        digit = result%10
        Newnode = Node(digit)
        if head is None:
            head = Newnode
            temp = head
        else:
            temp.next = Newnode
            temp = temp.next
        result = result//10
    return head


head1 = takeInput()
head2 = takeInput()
num1 = numberlist(head1)
num2 = numberlist(head2)
result = int(num1) + int(num2)
print(result)
head = newll(result)
printlist(head)
