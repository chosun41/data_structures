class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# may start and end at any node

# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 

max_sum = 0

def find_max_sum(root):

    global max_sum
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    left = find_max_sum(root.left)
    right = find_max_sum(root.right)
    cand = max(left,right)
    max_sum = max(max_sum, cand + root.val)
    return max_sum
    

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(find_max_sum(root))