import sys
sys.path.append('../queues')
from queues import Queue
from binary_tree import BinaryTree

def numberOfLeavesInBTusingLevelOrder(root):
    if root is None:
        return 0
    q = Queue()
    q.enqueue(root)
    node = None
    count = 0
    while not q.isEmpty():
        node = q.dequeue()  # dequeue FIFO
        
        # leaves has no left and right so increment here
        # can also find number of full nodes with not None here
        if node.left is None and node.right is None:
            count += 1
        else:
            if node.left is not None:
                q.enqueue(node.left)

            if node.right is not None:
                q.enqueue(node.right)
    return count
            
if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    print(numberOfLeavesInBTusingLevelOrder(root))