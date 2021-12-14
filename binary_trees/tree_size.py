from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findSizeRecursive(root): 
    if not root:
        return 0
    return findSizeRecursive(root.left) + findSizeRecursive(root.right) + 1

def findSizeusingLevelOrder(root):
    if root is None:
        return 0

    q = deque()
    q.append(root)
    node = None
    count = 0
    while q:
        node = q.popleft()  # dequeue FIFO
        count += 1
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    return count

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(findSizeRecursive(root))
    print(findSizeusingLevelOrder(root))

