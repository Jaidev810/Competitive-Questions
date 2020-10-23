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



def removezero(head):
    arr = []
    temp = head
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    st = []
        
    for i in range(0, len(arr)):
        if i == 0:
            st.append(arr[i])
            continue
        if st[-1] + arr[i] != 0:
            st.append(arr[i])
            continue
        else:
            while True:
                if len(st) == 0:
                    st.append(arr[i])
                    break
                elif st[-1] + arr[i] != 0:
                    st.append(arr[i])
                    break
                else:
                    st.pop()
                    break
    new_head = None
    temp = None
        
    for i in range(0, len(st)):
        new_node = Node(st[i])
        if new_head is None:
            new_head = new_node
            temp = new_head
        else:
            temp.next = new_node
            temp = temp.next
    return new_head
        
    

root = takeinput()
printLL(root)
new = removezero(root)
printLL(new)