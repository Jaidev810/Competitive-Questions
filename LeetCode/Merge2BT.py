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

    while not q.empty():
        curr_node = q.get()
        print('enter the Left child of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftChild = BinaryTree(leftData)
            curr_node.left = leftChild
            q.put(leftChild)

        print('enter thr right child of ', curr_node.data)
        rightData = int(input())
        if rightData != -1:
            rightChild = BinaryTree(rightData)
            curr_node.right = rightChild
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
            print('L', curr_node.left.data, end=',')
            q.put(curr_node.left)

        if curr_node.right is not None:
            print('R', curr_node.right.data, end='')
            q.put(curr_node.right)

        print()


def mergeTrees(root1, root2):
    if root1 is None and root2 is None:
        return None
    
    if root1 is not None and root2 is not None:
        root1.data = root1.data + root2.data

    elif root1 is None and root2 is not None:
        root1 = root2
        return root1
    
    elif root2 is None:
        return root1

    ltree = mergeTrees(root1.left, root2.left)
    rtree = mergeTrees(root1.right, root2.right)
    root1.left = ltree
    root1.right = rtree
    return root1

root1 = takeLevelwiseinput()
root2 = takeLevelwiseinput()
printLevelwise(root1)
printLevelwise(root2)
print()
printLevelwise(mergeTrees(root1, root2))