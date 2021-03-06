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


def SymmetricTree(root):
    if root is None:
        return True
    else:
        return helper(root.left, root.right)

def helper(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    if root1.data == root2.data:
        ltree = helper(root1.left, root2.right)
        rtree = helper(root1.right, root2.left)
        return ltree and rtree
    else:
        return False
    

    



root = takeLevelwiseinput()
printLevelwise(root)
print(SymmetricTree(root))