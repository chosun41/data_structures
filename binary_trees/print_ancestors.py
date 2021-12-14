class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printAncestors(root, target): 
      
    # Base case 
    if not root: 
        return False 
      
    if root.val == target: 
        return True 
  
    # If target is present in either left or right subtree  
    # of this node, then print this node 
    if (printAncestors(root.left, target) or 
        printAncestors(root.right, target)): 
        print(root.val) 
        return True
  
    # Else return False  
    return False
    
if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    printAncestors(root, 7)