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

class Solution:

    def helper(self, root, sum, arr):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.data == sum:
                arr += [root.data]
                self.ans.append(arr)
                return
        else:
            self.helper(root.left, sum - root.data, arr + [root.data])
            self.helper(root.right, sum - root.data, arr + [root.data])
    
    def pathSum(self, root, sum):
        self.ans = []
        self.helper(root, sum, [])
        return self.ans




root = takeLevelwiseInput()
sol = Solution()
ans = sol.pathSum(root, 22)
print(ans)
