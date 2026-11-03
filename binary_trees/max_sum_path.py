class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque

def find_max_sum(root):
    if not root:
        return 0
    q = deque()
    q.append([root, root.val])
    temp = 0
    while q:
        node, val= q.popleft()
        temp = max(temp, val)
        if node.left:
            q.append([node.left, val + node.left.val])
        if node.right:
            q.append([node.right, val + node.right.val])
    return temp
    

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(find_max_sum(root))