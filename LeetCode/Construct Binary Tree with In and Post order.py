import queue

class BinaryTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def takeLevelwiseInput():
    print('enter the root data: ')
    rootData = int(input())
    if rootData == -1:
        return None
    q = queue.Queue()
    root = BinaryTree(rootData)
    q.put(root)
    while not q.empty():
        curr_node = q.get()
        print('enter the Left child of ', curr_node.data)
        leftData = int(input())
        if leftData != -1:
            leftChild = BinaryTree(leftData)
            curr_node.left = leftChild
            q.put(curr_node.left)
        
        print('enter the Right child  of ', curr_node.data)
        rightData = int(input())
        if rightData != -1:
            rightChild = BinaryTree(rightData)
            curr_node.right = rightChild
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


def construct(inorder, postorder):
    Inlength = len(inorder)
    Postlength = len(postorder)
    if Inlength == 0 and Postlength == 0:
        return None
    rootData = postorder[-1]
    index = 0
    root = BinaryTree(rootData)
    for i in range(0, Inlength):
        if inorder[i] == rootData:
            index = i
            break
    leftIn = inorder[0:index]
    rightIn = inorder[index+1:]
    temp = len(leftIn)
    leftPost = postorder[0:temp]
    rightPost = postorder[temp:Postlength-1]
    root.left = construct(leftIn, leftPost)
    root.right = construct(rightIn, rightPost)
    return root


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = construct(inorder, postorder)
printLevelwise(root)