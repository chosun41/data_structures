class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# structurally same mean data doesn't have to agree, but the tree structure should be

def areStructurallySameTrees(root1, root2):
    
    # both have leaves, nothing more to process
    if not root1.left and not root1.right and not root2.left and not root2.right:
        return True
    
    # if one exists and not the other 
    if (root1.left and not root2.left) or (not root1.left and root2.left) or (root1.right and not root2.right) \
        or (not root1.right and root2.right): 
        return False

    # recursive on left and right
    left = areStructurallySameTrees(root1.left, root2.left) if root1.left and root2.left else True
    right = areStructurallySameTrees(root1.right, root2.right) if root1.right and root2.right else True
    
    # only true if both true
    return left and right
    
if __name__ == '__main__':
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    
    root2 = TreeNode(8)
    root2.left = TreeNode(9)
    root2.right = TreeNode(10)
    root2.left.left = TreeNode(11)
    root2.left.right = TreeNode(12)
    root2.right.left = TreeNode(13)
    
    print(areStructurallySameTrees(root1, root2))
