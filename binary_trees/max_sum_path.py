class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# may start and end at any node

# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 

globalMax = float("-inf") 

def find_max_sum(root):
    if not root:
        return 0

    # Recursive calls to children:
    left = find_max_sum(root.left)
    right = find_max_sum(root.right)

    # Max of first three cases:
    return_max = max(max(left, right) + root.val, root.val)

    # Update globalMax:
    global globalMax
    if return_max > globalMax:
        globalMax = return_max

    return globalMax

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(find_max_sum(root))