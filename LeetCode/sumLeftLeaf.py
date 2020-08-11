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


def helper(root, isLeft):

    if root:
        if root.left is None and root.right is None and isLeft:
            arr.append(root.data)

        
            
def SumofLeftLeaf(root):
    if root is None:
        return 0

    ltree = helper(root.left, True)
    rtree = helper(root.right, False)

root = takeLevelwiseinput()
printLevelwise(root)
print(SumofLeftLeaf(root))