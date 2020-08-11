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

    q = queue.Queue()
    root = BinaryTree(rootData)
    q.put(root)

    while not(q.empty()):
        curr_node = q.get()

        print('enter the leftchild of ', curr_node.data)
        leftdata = int(input())
        if leftdata != -1:
            leftchild = BinaryTree(leftdata)
            curr_node.left = leftchild
            q.put(leftchild)


        print('enter the rightchild of ', curr_node.data)
        rightdata = int(input())
        if rightdata != -1:
            rightchild = BinaryTree(rightdata)
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

def ZigZagLevel(root):
    if root is None:
        return None

    st = list()
    temp = list()
    arr = list()

    st.append(root)
    st.append(None)

    while len(st) != 0:
        curr_node = st.pop()
        if curr_node is None:
            if len(st) == 0 and len(temp) == 0:
                break
            elif len(temp) == 0:
                continue
            else:
                arr.append(temp)
                st.append(None)
                temp = []
        else:
            if curr_node.left is not None:
                st.append(curr_node.left)
            if curr_node.right is not None:
                st.append(curr_node.right)
            temp.append(curr_node.data)

    return arr


root = takeLevelwiseinput()
printLevelwise(root)

print(ZigZagLevel(root))

