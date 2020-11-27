import sys
sys.path.append('../queues')
from queues import Queue

# classic binary tree, no heirarchical order
class BinaryTree:
    
    def __init__(self, data):
        self.data = data  # root node
        self.left = None  # left child
        self.right = None  # right child
    # set data
    def set_data(self, data):
        self.data = data
    # get data   
    def get_data(self):
        return self.data
    # get left child of a node
    def getLeft(self):
        return self.left
    # get right child of a node
    def getRight(self):
        return self.right
    # get left child of a node
    def setLeft(self, left):
        self.left = left
    # get right child of a node
    def setRight(self, right):
        self.right = right
          
    def insertLeft(self, val):
        if self.left == None:
            self.left = BinaryTree(val)
        # makes current left a left of new left
        else:
            temp = BinaryTree(val)
            temp.left = self.left
            self.left = temp

    def insertRight(self, val):
        if self.right == None:
            self.right = BinaryTree(val)
        # makes current right a right of new right
        else:
            temp = BinaryTree(val)
            temp.right = self.right
            self.right = temp

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
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
            
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
 
    q = Queue()
    q.enqueue(root)
    n = None
 
    while not q.isEmpty():
      n = q.dequeue()  # dequeue FIFO
      result.append(n.get_data())
      if n.left is not None:
        q.enqueue(n.left)
 
      if n.right is not None:
        q.enqueue(n.right)
        
    return result

if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    root.getLeft().getLeft().insertLeft(8)
    root.getLeft().getLeft().insertRight(9)
    root.getLeft().getRight().insertLeft(10)
    root.getLeft().getRight().insertRight(11)
    root.getRight().getLeft().insertLeft(12)
    root.getRight().getLeft().insertRight(13)
    root.getRight().getRight().insertLeft(14)
    root.getRight().getRight().insertRight(15)
    
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
    
    
