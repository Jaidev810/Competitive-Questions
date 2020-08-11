import queue

class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeLevelwiseinput():
    print('enter the root data: ')
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)

    while not(q.empty()):
        curr_node = q.get()
        print('enter the leftchild of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftchild = BinaryTree(leftData)
            curr_node.left = leftchild
            q.put(leftchild)

        print('enter the rightchild of ', curr_node.data)
        rightData = int(input())
        if rightData != -1:
            rightchild = BinaryTree(rightData)
            curr_node.right = rightchild
            q.put(rightchild)

    return root


def printLevelwise(root):
    if root is None:
        return None
    
    q = queue.Queue()
    q.put(root)

    while not(q.empty()):
        curr_node = q.get()
        print(curr_node.data, end=':')

        if curr_node.left is not None:
            print('L', curr_node.left.data, end=',')
            q.put(curr_node.left)
        
        if curr_node.right is not None:
            print('R', curr_node.right.data, end='')
            q.put(curr_node.right)

        print()


def bottomLevelOrder(root):
    if root is None:
        return None

    temp = []
    arr = []
    q = list()
    q.append(root)
    q.append(None)

    while len(q) != 0:
        curr_node = q.pop(0)
        if curr_node is None:
            arr.append(temp)
            temp = []
            if len(q) == 0:
                break
            else:
                q.append(None)
                continue
        
        if curr_node.left is not None:
            q.append(curr_node.left)
        if curr_node.right is not None:
            q.append(curr_node.right)

        temp.append(curr_node.data)

    
    arr1 = list()
    for i in range(len(arr)-1, -1, -1):
        arr1.append(arr[i])

    return arr1


root = takeLevelwiseinput()
printLevelwise(root)
arr = bottomLevelOrder(root)
print(arr)