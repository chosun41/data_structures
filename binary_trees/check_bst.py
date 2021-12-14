class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def IsBST(root, min, max):
    
    # shrinking min and max with each recursive calls
    
    # reached end
    if not root:
        return True
    # outside of min and max bounds
    if root.val <= min or root.val >= max:
        return False
    # min < root.left < root
    left = IsBST(root.left, min, root.val)
    # root < root.right < max
    right = IsBST(root.right, root.val, max)
    
    return left and right

if __name__ == '__main__':
    
    # time: O(n)
    # space: O(n)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    
    #    1
    #  2   3
    # 4 5 6 7
    
    print(IsBST(root1,-float("infinity"),float("infinity")))
    
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(7)
    
    #      4
    #   2    6
    # 1  3 5   7
    
    print(IsBST(root2,-float("infinity"),float("infinity")))