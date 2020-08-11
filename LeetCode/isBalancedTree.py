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


def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)

def isBalancedTree(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return 1
    lh = height(root.left)
    rh = height(root.right)
    if lh == rh or -1 < rh-lh <=1 or  -1 < lh-rh <=1:
        if isBalancedTree(root.left):
            if isBalancedTree(root.right):
                return True
            else:
                return False
        else:
            return False
    
    return False


root = takeLevelwiseinput()
printLevelwise(root)
if isBalancedTree(root):
    print('true')
else:
    print('False')
