import queue
class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def takeLevelwiseinput():
    print('enter the root Data:')
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
    
def minNode(root):
    if root is None:
        return 1000000
    if root.left is None:
        return root.data
    return minNode(root.left)

def deleteNode(root, x):
    if root is None:
        return None
    
    if root.data > x:
        root.left = deleteNode(root.left, x)
        return root
    elif root.data > x:
        root.right = deleteNode(root.right, x)
        return root
    else:
        #if no children
        if root.left is None and root.right is None:
            return None
        
        #if one children
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # two children
        else:
            replace = minNode(root.right)
            root.data = replace
            root.right = deleteNode(root.right, replace)
            return root

