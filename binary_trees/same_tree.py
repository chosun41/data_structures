from binary_tree import BinaryTree

# structurally same mean data doesn't have to agree, but the tree structure should be

def areStructurullySameTrees(root1, root2):
    
    # both have leaves, nothing more to process
    if not root1.left and not root1.right and not root2.left and not root2.right:
        return True
    
    # if one exists and not the other 
    if (root1.left and not root2.left) or (not root1.left and root2.left) or (root1.right and not root2.right) \
        or (not root1.right and root2.right): 
        return False

    # recursive on left and right
    left = areStructurullySameTrees(root1.left, root2.left) if root1.left and root2.left else True
    right = areStructurullySameTrees(root1.right, root2.right) if root1.right and root2.right else True
    
    # only true if both true
    return left and right
    
if __name__ == '__main__':
    
    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.insertRight(3)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    root1.getRight().insertLeft(6)
#     root1.getRight().insertRight(7)
    
    root2 = BinaryTree(8)
    root2.insertLeft(9)
    root2.insertRight(10)
    root2.getLeft().insertLeft(11)
    root2.getLeft().insertRight(12)
    root2.getRight().insertLeft(13)
#     root2.getRight().insertRight(14)
    
    print(areStructurullySameTrees(root1, root2))
