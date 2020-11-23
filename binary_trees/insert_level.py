import sys
sys.path.append('../queues')
from queues import Queue
from binary_tree import BinaryTree,levelOrder

def insertInBinaryTreeUsingLevelOrder(root, data):
    newNode = BinaryTree(data)
    if root is None:
        root = newNode
        return root

    q = Queue()
    q.enqueue(root)
    node = None
    while not q.isEmpty():
        node = q.dequeue()  # dequeue FIFO

        if data == node.get_data():
            return root
        
        # basically level order, insert would be where there is no left
        if node.left is not None:
            q.enqueue(node.left)
        else:
            node.left = newNode
            return root	
        # if left all filled, insert right
        if node.right is not None:
            q.enqueue(node.right)
        else:
            node.right = newNode
            return root
            
if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    root = insertInBinaryTreeUsingLevelOrder(root, 8)
    
    print(levelOrder(root,[]))