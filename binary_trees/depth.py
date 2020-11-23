from binary_tree import BinaryTree

def maxDepthRecursive(root):
    if root == None:
        return 0
    return max(maxDepthRecursive(root.getLeft()), maxDepthRecursive(root.getRight())) + 1

def maxDepthLevelOrder(root):
    if root == None:
        return 0
    q = []
    q.append([root, 1])
    temp = 0
    while len(q) != 0:
        node, depth = q.pop()
        temp = max(temp, depth)
        if node.getLeft() != None:
            q.append([node.getLeft(), depth + 1])
        if node.getRight() != None:
            q.append([node.getRight(), depth + 1])
    return temp

if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    print(maxDepthRecursive(root))
    print(maxDepthLevelOrder(root))