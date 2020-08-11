import queue
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = list()

def takeLevelwiseinput():
    print('enter the root Data:')
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q = queue.Queue()
    q.put(root)
    while not(q.empty()):
        curr_node = q.get()
        print('enter the number of children: ', curr_node.data)
        numchild = int(input())
        for i in range(numchild):
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
            print(curr_node.children[i].data, end=',')
            q.put(curr_node.children[i])

        print()

def maxDepth(root):
    if root is None:
        return 0
    q = list()
    q.append(root)
    q.append(None)
    depth = 0
    while len(q) != 0:
        curr_node = q.pop(0)
        if curr_node is None:
            depth += 1
            if len(q) == 0:
                break
            else:
                q.append(None)
                continue
        numChild = len(curr_node.children)
        for i in range(numChild):
            q.append(curr_node.children[i])
        
    return depth

root = takeLevelwiseinput()
printLevelwise(root)
print(maxDepth(root))