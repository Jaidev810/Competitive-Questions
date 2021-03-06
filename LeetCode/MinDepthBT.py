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

def helper(root):
    if root is None:
        return 0
    elif root.left is None and root.right is not None:
        rh = helper(root.right)
        return 1 + rh
    elif root.right is None and root.left is not None:
        lh = helper(root.left)
        return 1 + lh
    else:
        lh = helper(root.left)
        rh = helper(root.right)
        return 1 + min(lh, rh)


def minDepth(root):
    if root is None:
        return 0
    elif root.left is None and root.right is not None:
        rh = helper(root.right)
        return 1 + rh
    elif root.right is None and root.left is not None:
        lh = helper(root.left)
        return 1 + lh
    else:
        lh = helper(root.left)
        rh = helper(root.right)
        return 1 + min(lh, rh)



root = takeLevelwiseinput()
printLevelwise(root)
print(minDepth(root))