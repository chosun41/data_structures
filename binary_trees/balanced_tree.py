from binary_tree import BinaryTree

# check if tree is balanced
# height balanced if at most the difference b/t left and right subtrees is at most one
# does not have to a perfect or complete binary tree

def height(root):
    if (root == None) :
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root): 
      
    # Base condition 
    if root is None: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and isBalanced( 
    root.left) is True and isBalanced(root.right) is True: 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False
    
if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    print(isBalanced(root))
    
    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    
    print(isBalanced(root1))
    