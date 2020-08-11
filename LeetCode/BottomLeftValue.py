#Binary Tree
import queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def takeLevelwiseInput():
    print('enter the root:')
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)
    while not(q.empty()):
        curr_node = q.get()
        print('enter the leftChild of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftchild = BinaryTree(leftData)
            curr_node.left = leftchild
            q.put(curr_node.left)
        
        print('enter the rightChild of ', curr_node.data)
        rightData = int(input())
        if rightData != -1:
            rightchild = BinaryTree(rightData)
            curr_node.right = rightchild
            q.put(curr_node.right)
    return root


def printLevelWise(root):
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
        return 0, None
    if root.left is None:
        return 1, root
    lh, lchild = helper(root.left)
    rh, rchild = helper(root.right)
    if rh > lh:
        return rh+1, rchild
    else:
        return lh+1, lchild



def BottomLeft(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    lh, lchild = helper(root.left)
    rh, rchild = helper(root.right)
    if lh > rh:
        return lchild.data
    elif rh > lh:
        return rchild.data
    else:
        return lchild.data

root = takeLevelwiseInput()
printLevelWise(root)
print(BottomLeft(root))