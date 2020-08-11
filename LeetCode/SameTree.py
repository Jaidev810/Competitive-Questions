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


def SameTree(p, q):
    if p is None and q is None:
        return None
    
    q1 = list()
    q2 = list()

    q1.append(p)
    q2.append(q)

    while len(q1) != 0 and len(q2) != 0:
        curr1 = q1.pop(0)
        curr2 = q2.pop(0)

        if curr1 is not None and curr2 is not None:
            if curr1.data != curr2.data:
                return False

            q1.append(curr1.left)
            q1.append(curr1.right)
            q2.append(curr2.left)
            q2.append(curr2.right)
        
        if curr1 is None and curr2 is not None:
            return False
        if curr1 is not None and curr2 is None:
            return False

    return True

p = takeLevelwiseinput()
q = takeLevelwiseinput()
printLevelwise(p)
printLevelwise(q)
print(SameTree(p, q))