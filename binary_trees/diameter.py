from binary_tree import BinaryTree

# diameter is the number of nodes along the longest path b/t any two nodes 
# basically get the max height from left and right

def diameter(root):
    if (root == None): 
        return 0

    lHeight = height(root.left)
    rHeight = height(root.right)
    lDiameter = diameter(root.left)
    rDiameter = diameter(root.right)
    return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))

def height(root):
    if (root == None) :
        return 0
    return 1 + max(height(root.left), height(root.right))

if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    print(diameter(root))
    print(height(root))
