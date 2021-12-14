class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque

# sum all nodes in tree

def sumInBinaryTreeRecursive(root):
    if not root :
        return 0
    return root.val + sumInBinaryTreeRecursive(root.left) + sumInBinaryTreeRecursive(root.right)

def sumInBinaryTreeLevelOrder(root):
    if not root:
        return 0
    q = deque()
    q.append(root)
    node = None
    sum = 0
    while q:
        node = q.popleft()  # dequeue FIFO
        if node:
            sum += node.val
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
    return sum
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(sumInBinaryTreeRecursive(root))
    print(sumInBinaryTreeLevelOrder(root))