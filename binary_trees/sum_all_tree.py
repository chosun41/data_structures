import sys
sys.path.append('../queues')
from queues import Queue
from binary_tree import BinaryTree

# sum all nodes in tree

def sumInBinaryTreeRecursive(root):
    if(root == None) :
           return 0
    return root.data + sumInBinaryTreeRecursive(root.left) + sumInBinaryTreeRecursive(root.right)

def sumInBinaryTreeLevelOrder(root):
    if root is None:
        return 0
    q = Queue()
    q.enqueue(root)
    node = None
    sum = 0
    while not q.isEmpty():
        node = q.dequeue()  # dequeue FIFO
        sum += node.get_data()
        if node.left is not None:
            q.enqueue(node.left)

        if node.right is not None:
            q.enqueue(node.right)
    return sum
    
if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    print(sumInBinaryTreeRecursive(root))
    print(sumInBinaryTreeLevelOrder(root))