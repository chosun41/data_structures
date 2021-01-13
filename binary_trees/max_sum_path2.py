class TreeNode:
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def maxPathSum2(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0

        # max sum on the left and right sub-trees of node
        left_gain = max_gain(node.left)
        right_gain = max_gain(node.right)

        # update max_sum if it's better to start a new path
        max_sum = max(max_sum, node.val + left_gain + right_gain)

        # for recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum

if __name__=='__main__':
    
    # time: O(n) # of nodes
    # space: O(h) tree height
    # here path is not from root to leaves but from any node from left to right
    x=TreeNode(-10)
    x.left=TreeNode(9)
    x.right=TreeNode(20)
    x.right.left=TreeNode(15)
    x.right.right=TreeNode(7)
    print(maxPathSum2(x))