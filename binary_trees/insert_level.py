class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque

def insertInBinaryTreeUsingLevelOrder(root, data):
    newNode = TreeNode(data)
    if not root:
        root = newNode
        return root

    q = deque()
    q.append(root)
    node = None
    while q:
        node = q.popleft()  # dequeue FIFO

        if data == node.val:
            return root
        
        # basically level order, insert would be where there is no left
        if node.left:
            q.append(node.left)
        else:
            node.left = newNode
            return root	
        # if left all filled, insert right
        if node.right:
            q.append(node.right)
        else:
            node.right = newNode
            return root
            
if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root = insertInBinaryTreeUsingLevelOrder(root, 8)
    print(root.left.left.left.val)
    
