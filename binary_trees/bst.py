from copy import deepcopy
import sys
sys.path.append('../queues')
from queues import Queue

# bst is different from binary tree in that to the left is < and to the right > root value

class BST:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
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

    def insert(self, val):
        if val < self.data:
            if self.left == None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right == None:
                self.right = BST(val)
            else:
                self.right.insert(val)
            
    # return self if val equals current node data
    # else look recursively left and right based on comparisons
    # if all else fails return None
    def find(self, val):
        if val == self.data:
            return self
        elif val < self.data:
            return self.left.find(val)
        else:
            return self.right.find(val)
        return None
    
    # keep going left until end
    def find_min(self):
        curr = self
        while curr.left:
            curr=curr.left
        return curr.data
    
    # keep going right until end
    def find_max(self):
        curr = self
        while curr.right:
            curr=curr.right
        return curr.data

    # Given a non-empty binary 
    # search tree, return the node
    # with minum key value 
    # found in that tree. Note that the
    # entire tree does not need to be searched

    def minValueNode(self):
        current = self

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    # Given a binary search tree and a key, this function
    # delete the key and returns the new root


    def delete(self, val):

        # If the key to be deleted 
        # is smaller than the root's
        # key then it lies in  left subtree
        if val < self.data:
            self.left = self.left.delete(val)

        # If the kye to be delete 
        # is greater than the root's key
        # then it lies in right subtree
        elif(val > self.data):
            self.right = self.right.delete(val)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Node with two children: 
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.right.minValueNode()

            # Copy the inorder successor's 
            # content to this node
            self.data = temp.data

            # (recursively) Delete the inorder successor
            # you are replacing with minimum value (left most item) in the right subtree - successor
            self.right = self.right.delete(temp.data)

        return self

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
        result.append(n.data)
        if n.left is not None:
        q.enqueue(n.left)

        if n.right is not None:
        q.enqueue(n.right)
        
    return result

# leftmost of right subtree
def successorBST(root):
    temp = None
    if root.getRight():
        temp = root.getRight()
        while temp.getLeft():
            temp = temp.getLeft()
    return temp

# rightmost of left subtree
def predecessorBST(root):
    temp = None
    if root.getLeft():
        temp = root.getLeft()
        while temp.getRight():
            temp = temp.getRight()
    return temp

if __name__ == '__main__':
    
    root = BST(4)
    root.insert(2)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(7)
    
    #      4
    #   2    6
    # 1  3 5   7
    
    print(levelOrder(root,[]))
    
    x=root.find(6)
    print(x.left.data)
    print(x.right.data)
    print("\n")
    
    y=root.find(2)
    print(y.left.data)
    print(y.right.data)
    print("\n")
    
    print(root.find_min())
    print(root.find_max())
    print("\n")
    
    a=deepcopy(root)
    a.delete(7)
    print(levelOrder(a,[]))
    
    b=deepcopy(root)
    b.delete(3)
    print(levelOrder(b,[]))
    
    c=deepcopy(root)
    c.delete(6)
    print(levelOrder(c,[]))
    
    d=deepcopy(root)
    d.delete(2)
    print(levelOrder(d,[]))
    
    e=deepcopy(root)
    e.delete(4)
    print(levelOrder(e,[]))
    
    print(successorBST(root).data)
    print(predecessorBST(root).data)
    

