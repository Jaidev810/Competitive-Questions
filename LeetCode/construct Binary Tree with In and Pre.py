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


def buildTree(preorder, inorder):
    Prelength = len(preorder)
    Inlength = len(inorder)
    if Prelength == 0 and Inlength == 0:
        return None
    
    rootData = preorder[0]
    root = BinaryTree(rootData)
    index = 0
    for i in range(0, Inlength):
        if inorder[i] == rootData:
            index = i
            break
    leftIn = inorder[0:index]
    rightIn = inorder[index+1:]
    temp = len(leftIn)
    leftPre = preorder[1:temp+1]
    rightPre = preorder[temp+1:]
    root.left = buildTree(leftPre, leftIn)
    root.right = buildTree(rightPre, rightIn)
    return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = buildTree(preorder, inorder)
printLevelwise(root)

