class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
def takeinputLL():
    print('enter the linked list data:')
    inputlist = [int(x) for x in input().split()]
    head = None
    temp = None
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

def lengthLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

# for Tree  
import queue
class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def takeLevelwiseInput():
    print("enter root's data: ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print('enter the left child of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftchild = BinaryTree(leftData)
            curr_node.left = leftchild
            q.put(curr_node.left)

        print('enter the right child of ', curr_node.data)
        rightData = int(input())
        if rightData != -1:
            rightchild = BinaryTree(rightData)
            curr_node.right = rightchild
            q.put(curr_node.right)
    return root

def printLevelwise(root):
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print(curr_node.data, end=':')
        if curr_node.left is not None:
            print(curr_node.left.data, end=',')
            q.put(curr_node.left)
        
        if curr_node.right is not None:
            print(curr_node.right.data, end='')
            q.put(curr_node.right)
        print()

def helper(arr):
    size = len(arr)
    if size == 0:
        return None
    if size%2 == 0:
        mid = size//2 -1
    else:
        mid = size//2
    root = BinaryTree(arr[mid])
    root.left = helper(arr[0:mid])
    root.right = helper(arr[mid+1:])
    return root


def constructBST(head):
    arr = []
    while head is not None:
        arr.append(head.data)
        head = head.next
        
    root = helper(arr)
    return root
    
head = takeinputLL()
root = constructBST(head)
printLevelwise(root)

