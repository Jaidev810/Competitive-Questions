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



def PathSum(root, k):
    if root is None:
        return False
    
    if k == root.data and root.right is None and root.left is None:
        return True
    
    left = PathSum(root.left, k-root.data)
    if left:
        return True
    else:
        right = PathSum(root.right, k - root.data)
        if right:
            return True
        else:
            return False
    
    return False






root = takeLevelwiseinput()
printLevelwise(root)
sum = 22
if PathSum(root, sum):
    print('true')
else:
    print('false')