from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# depth of binary tree

def maxDepthRecursive(root):
    if not root:
        return 0
    return max(maxDepthRecursive(root.left), maxDepthRecursive(root.right)) + 1

def maxDepthLevelOrder(root):
    if not root:
        return 0
    q = deque()
    q.append([root, 1])
    temp = 0
    while q:
        node, depth = q.popleft()
        temp = max(temp, depth)
        if node.left:
            q.append([node.left, depth + 1])
        if node.right:
            q.append([node.right, depth + 1])
    return temp

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(maxDepthRecursive(root))
    print(maxDepthLevelOrder(root))