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


def isValidBst(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True

    temp = root.data
    ltree = isValidBst(root.left)
    if ltree:
        if root.left is not None and root.left.data < root.data and root.left.data < temp:
            rtree = isValidBst(root.right)
            if rtree:
                if root.right is not None and root.right.data > root.data and root.right.data > temp:
                    return True
                elif root.right is None:
                    return True
                else:
                    return False
        elif root.left is None:
            rtree = isValidBst(root.right)
            if rtree:
                if root.right is not None and root.right.data > root.data and root.right.data > temp:
                    return True
                elif root.right is None:
                    return True
                else:
                    return False
        else:
            return False


root = takeLevelwiseinput()
printLevelwise(root)
print(isValidBst(root))