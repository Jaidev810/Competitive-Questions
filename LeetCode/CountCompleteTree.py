import queue

class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeLevelwiseInput():
    print('enter the rootData:')
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print('enter the left child of ', curr_node.data)
        leftdata = int(input())
        if leftdata != -1:
            leftchild = BinaryTreeNode(leftdata)
            curr_node.left = leftchild
            q.put(leftchild)

        print('enter the right child of ', curr_node.data)
        rightdata = int(input())
        if rightdata != -1:
            rightchild = BinaryTreeNode(rightdata)
            curr_node.right = rightchild
            q.put(rightchild)

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

def countCompleteNodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    ltree = countCompleteNodes(root.left)
    rtree = countCompleteNodes(root.right)
    return 1 + ltree + rtree


root = takeLevelwiseInput()
printLevelwise(root)
print(countCompleteNodes(root))
