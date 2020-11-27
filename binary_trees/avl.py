import sys
sys.path.append('../queues')
from queues import Queue

# avl is balanced binary search tree to ensure search is O(log n) since 
# trees can become skewed in which case search is O(n)

# the height of the left and right subtree differ by at most 1
# balanceFactor = height of right - height of left need to be -1,0,1 else it rebalances 

# Create a tree node
class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree():

    # Function to insert a node        
    def insert_node(self, root,data):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(data)
        # recursively look left and right depending ond ata comparisons
        elif data < root.data:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        
        if balanceFactor > 1:
            if data < root.left.data:
                return self.rightRotate(root)
            else:
                # left right rotation
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if data > root.right.data:
                return self.leftRotate(root)
            else:
                # right left rotation
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, data):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,
                                          temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the subtree from node down
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

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
    
if __name__ == '__main__':
    
    avl = AVLTree()
    
    root = None
    data = [3, 1, 9, 6, 0, 11, 2, 5, 4]

    for d in data:      
        root = avl.insert_node(root,d)
        print(levelOrder(root,[]))
    
    #        3
    #   1          9
    # 0   2     5    11 
    #         4   6

    root = avl.delete_node(root,9)
    print(levelOrder(root,[]))
    
    #        3
    #   1          5
    # 0   2     4    11 
    #             6
    
    root = avl.delete_node(root,1)
    print(levelOrder(root,[]))
    
    #        3
    #    2        5
    # 0        4    11 
    #             6