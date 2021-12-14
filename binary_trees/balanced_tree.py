# check if tree is balanced
# height balanced if at most the difference b/t left and right subtrees is at most one
# does not have to a perfect or complete binary tree

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def isBalanced(root): 
      
    # Base condition 
    if not root: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and isBalanced(root.left) is True and isBalanced(root.right) is True: 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False
    
if __name__ == '__main__':

    # time and space: O(n)
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(isBalanced(root))
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    
    print(isBalanced(root1))
    