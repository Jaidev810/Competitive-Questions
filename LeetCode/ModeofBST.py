import queue
import sys
class BST:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def takeInputLevel():

    print('enter the root data:')
    rootData = int(input())
    if rootData == -1:
        return
    
    root = BST(rootData)
    q = queue.Queue()

    q.put(root)

    while not(q.empty()):
        temp = q.get()

        print('enter the left child:', temp.data)
        leftData = int(input())
        if leftData != -1:
            leftchild = BST(leftData)
            temp.left = leftchild
            q.put(leftchild)

        print('enter the right child: ', temp.data)
        rightdata = int(input())
        if rightdata != -1:
            rightchild = BST(rightdata)
            temp.right = rightchild
            q.put(rightchild)

    return root


def printLevelwise(root):
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)

    while not(q.empty()):
        temp = q.get()

        print(temp.data, end=':')

        if temp.left is not None:
            print('L', temp.left.data, end=',')
            q.put(temp.left)
        if temp.right is not None:
            print('R', temp.right.data, end='')
            q.put(temp.right)
        print()

def Mode(root):
    if root is None:
        return None

    q = queue.Queue()
    d = dict()

    q.put(root)

    while not q.empty():
        temp = q.get()
        d[temp.data] = d.get(temp.data, 0) + 1

        if temp.left is not None:
            q.put(temp.left)
        if temp.right is not None:
            q.put(temp.right)

    max = -sys.maxsize
    for i in d:
        if d[i] > max:
            max = d[i]
    
    arr = []
    for i in d:
        if d[i] == max:
            arr.append(i)

    print(arr)


root = takeInputLevel()
printLevelwise(root)
Mode(root)
