import queue

class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def takeLevelwiseInput():
    print("enter root's data: ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print('enter the left child of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftchild = BinaryTree(leftData)
            curr_node.left = leftchild
            q.put(curr_node.left)

        print('enter the right child of ', curr_node.data)
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
    while not q.empty():
        curr_node = q.get()
        print(curr_node.data, end=':')
        if curr_node.left is not None:
            print(curr_node.left.data, end=',')
            q.put(curr_node.left)
        
        if curr_node.right is not None:
            print(curr_node.right.data, end='')
            q.put(curr_node.right)
        print()



def levelorder(root):
    arr =[]
    q = []
    if root is None:
        return None
    q.append(root)
    q.append(None)
    temp = []
    while len(q) != 0:
        curr_node = q.pop(0)
        if curr_node is None:
            if len(q) == 0 and len(temp) == 0:
                break
            else:
                arr.append(temp)
                temp = []
                q.append(None)
        else:
            if curr_node.left is not None:
                q.append(curr_node.left)

            if curr_node.right is not None:
                q.append(curr_node.right)
            
            temp.append(curr_node.data)
    return arr


root = takeLevelwiseInput()
arr = levelorder(root)
print(arr)