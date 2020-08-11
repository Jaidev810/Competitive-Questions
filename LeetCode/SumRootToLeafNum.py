import queue
class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def takeLevelwiseinput():
    print('enter the root data:')
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
            q.put(curr_node.left)

        print('enter the rightchild of ', curr_node.data)
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


def helper(root, root_val, arr):
    if not root.left and not root.right:
        arr.append(root_val)

    if root.left:
        left = helper(root.left, root_val + str(root.left.data), arr)
    
    if root.right:
        right = helper(root.right, root_val + str(root.right.data), arr)

    return arr


def SumRootLeaf(root):
    if root is None:
        return 0

    arr = helper(root, str(root.data), [])
    return arr

root = takeLevelwiseinput()
printLevelwise(root)
print(SumRootLeaf(root))