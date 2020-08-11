import queue
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = list()

def takeLevelwiseInput():
    print('enter the root:')
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)

    q = queue.Queue()
    q.put(root)
    while not(q.empty()):
        curr_node = q.get()
        print('enter the number of children:', curr_node.data)
        numChild = int(input())

        for i in range(numChild):
            print('enter the data of ', curr_node.data)
            childData = int(input())
            child = TreeNode(childData)
            curr_node.children.append(child)
            q.put(child)
    
    return root


def printLevelwise(root):
    if root is None:
        return None
    
    q = queue.Queue()
    q.put(root)

    while not(q.empty()):
        curr_node = q.get()
        print(curr_node.data, end=':')

        numchild = len(curr_node.children)
        for i in range(numchild):
            print(curr_node.children[i].data, end=',' )
            q.put(curr_node.children[i])
        
        print()

def helper(root, arr):
    q = list()

    if root is None:
        return None

    q.append(root)
    q.append(None)
    temp = []
    while len(q) != 0:
        curr_node = q.pop(0)
        if curr_node is None:
            arr.append(temp)
            temp = []
            if len(q) == 0:
                break
            else:
                q.append(None)
                continue
        numchild = len(curr_node.children)
        for i in range(numchild):
            q.append(curr_node.children[i])

        temp.append(curr_node.data)

    return arr


def LevelOrderTraversal(root):
    arr = []
    arr = helper(root, [])
    return arr

root = takeLevelwiseInput()
printLevelwise(root)
arr = LevelOrderTraversal(root)
print(arr)