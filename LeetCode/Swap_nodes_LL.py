class Node:
    def __init__(self, data:int, next=None):
        self.val = data
        self.next = next


class Solution:
    def inputLL(self):
        inp = [int(x) for x in input().split()]
        head = None
        temp = None

        for cur in inp:
            if cur == -1:
                break
            Newnode = Node(cur)
            if head is None:
                head = Newnode
                temp = head
            else:
                temp.next = Newnode
                temp = temp.next

        return head

    def printLL(self, head):
        while head:
            print(head.val, end='->')
            head = head.next
        print("None")


    def swapNodes(self, head:Node, k:int) -> Node:
        arr = list()
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next
        n = len(arr)
        arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
        head = None
        for cur in arr:
            Newnode = Node(cur)
            if head is None:
                head = Newnode
                pointer = head
            else:
                pointer.next = Newnode
                pointer = pointer.next

        return head


obj = Solution()
head = obj.inputLL()
obj.printLL(head)
k = 2
new_head = obj.swapNodes(head, k)
obj.printLL(new_head)

