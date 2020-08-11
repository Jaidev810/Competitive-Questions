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

def toDecimal(arr):
    if len(arr) == 0:
        return arr
    for i in range(len(arr)):
        n = arr[i]
        rev = 0
        j = 0
        while n!=0:
            digit = n%10
            rev = rev + digit*(2**j)
            n = n//10
            j += 1

        arr[i] = rev

    return arr


def helper(root, root_val,arr):
    if root.left is None and root.right is None:
        arr.append(root_val)

    if root.left is not None:
        helper(root.left, root_val + str(root.left.data), arr)
    if root.right is not None:
        helper(root.right, root_val + str(root.right.data), arr)

    return arr    

def SumToRoot(root):
    arr = []
    arr = helper(root, str(root.data), [])
    
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    arr = toDecimal(arr)
    sum = 0
    for i in arr:
        sum = sum + i
    return sum


root = takeLevelwiseinput()
printLevelwise(root)
print(SumToRoot(root))