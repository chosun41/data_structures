class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def rangeSumBST(root, L, R):

    res = 0
    if not root:
        return 0
    elif root.val<L or root.val>R:
        return 0
    elif L<=root.val<=R:
        res+=root.val
        res+=rangeSumBST(root.left, L, root.val)
        res+=rangeSumBST(root.right, root.val, R)

    return res

if __name__=='__main__':
    
    # time: O(n)
    # space: O(n)
    
    # sum all within range of values in bst
    
    x=TreeNode(10)
    x.left=TreeNode(5)
    x.right=TreeNode(15)
    x.left.left=TreeNode(3)
    x.left.right=TreeNode(7)
    x.right.right=TreeNode(18)
    
    print(rangeSumBST(x,5,15))