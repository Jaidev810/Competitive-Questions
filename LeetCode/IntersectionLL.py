class LL:

    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    print('enter the head:')
    inputlist = [int(x) for x in input().split()]

    head = None
    temp = None

    for curr in inputlist:
        if curr == -1:
            break

        Newnode = LL(curr)
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

def length(head):
    count  = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def intersectionLL(list1, list2):
    temp1 = list1
    temp2 = list2
    ans  = 0
    address = dict()
    ll1 = length(list1)
    ll2 = length(list2)

    for i in range(ll1):
        address[temp1] = temp1.data
        temp1 = temp1.next

    print(address)
    for i in range(ll2):
        print(temp2)
        if temp2.data in address.values():
            ans = temp2.data
            break
        temp2 = temp2.next


    return ans


head1 = takeInput()
head2 = takeInput()
ans = intersectionLL(head1, head2)
print(ans)