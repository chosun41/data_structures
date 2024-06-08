from collections import deque

class BinaryTree:
    
    def __init__(self, data):
        self.data = data  # root node
        self.left = None  # left child
        self.right = None  # right child

# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order (D L R)
def preorderRecursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)
    
    return result

# In-order recursive traversal. The nodes' values are appended to the result list in traversal order (L D R)
def inorderRecursive(root, result):
    if not root:
        return

    inorderRecursive(root.left, result)
    result.append(root.data)
    inorderRecursive(root.right, result)
    
    return result

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order (L R D)
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
    result.append(root.data)
    
    return result

# Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order (D L R)
def preorderIterative(root, result):
    if not root:
        return

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right: 
            stack.append(node.right)
        if node.left: 
            stack.append(node.left)
            
    return result

# In-order iterative traversal. The nodes' values are appended to the result list in traversal order (L D R)
def inorderIterative(root, result):
    if not root:
        return

    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right
            
    return result

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order (L R D)
def postorderIterative(root, result):
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            # if same as preorder
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None
                
    return result

def levelOrder(root, result):
    if root is None:
        return
 
    q = deque()
    q.append(root)
    n = None
 
    while q:
        n = q.popleft()  # dequeue FIFO
        result.append(n.data)
        if n.left is not None:
            q.append(n.left)

        if n.right is not None:
            q.append(n.right)
        
    return result

if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.right = BinaryTree(9)
    root.left.right.left = BinaryTree(10)
    root.left.right.right = BinaryTree(11)
    root.right.left.left = BinaryTree(12)
    root.right.left.right = BinaryTree(13)
    root.right.right.left = BinaryTree(14)
    root.right.right.right = BinaryTree(15)
    
    #           1 
    #      2          3
    #   4    5     6     7
    # 8  9 10 11 12 13 14 15
    
    print(preorderRecursive(root,[]))
    print(preorderIterative(root,[]))
    print(inorderRecursive(root,[]))
    print(inorderIterative(root,[]))
    print(postorderRecursive(root,[]))
    print(postorderIterative(root,[]))
    print(levelOrder(root,[]))
    
    
