class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return
    if p.val < root.val:
        return inorderSuccessor(root.left,p) or root
    else:
        return inorderSuccessor(root.right,p)
    
if __name__=='__main__':
    x=TreeNode(5)
    x.left=TreeNode(3)
    x.left.left=TreeNode(2)
    x.left.right=TreeNode(4)
    x.right=TreeNode(7)
    x.right.left=TreeNode(6)
    x.right.right=TreeNode(8)


    #    5
    #  3   7
    # 2 4 6  8 
    # in order for bst
    
    print(inorderSuccessor(x,x.left.right).val)
    print(inorderSuccessor(x,x.left).val)
    print(inorderSuccessor(x,x.right.left).val)