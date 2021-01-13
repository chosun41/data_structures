class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def maxAncestorDiff(root):
    if not root:
        return 0

    def helper(node, cur_max, cur_min):
        # if encounter leaves, return the max-min along the path
        if not node:
            return cur_max - cur_min
        # else, update max and min
        # and return the max of left and right subtrees
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        left = helper(node.left, cur_max, cur_min)
        right = helper(node.right, cur_max, cur_min)
        return max(left, right)

    return helper(root, root.val, root.val)
    
if __name__=='__main__':
    
    # time and space: O(n)
    # basically recurse and record max min of all paths from root to leaves
    x=TreeNode(8)
    x.left=TreeNode(3)
    x.right=TreeNode(10)
    x.left.left=TreeNode(1)
    x.left.right=TreeNode(6)
    x.left.right.left=TreeNode(4)
    x.left.right.right=TreeNode(7)
    x.right.right=TreeNode(14)
    x.right.right.left=TreeNode(13)
    
    #       8
    #    3     10
    # 1   6        14
    #    4  7    13
    
    print(maxAncestorDiff(x)) # 8-1 max diff