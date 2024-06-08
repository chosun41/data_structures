class TreeNode():
    
    def __init__(self,s,left=None,right=None):
        self.val = s
        self.left=left
        self.right=right

def maximumAverageSubtree(root):
    res = float('-inf')
    def dfs(node):
        nonlocal res
        if not node:
            return (0, 0)
        left_sum, left_cnt = dfs(node.left)
        right_sum, right_cnt = dfs(node.right)
        total = node.val + left_sum + right_sum
        cnt = left_cnt + right_cnt + 1
        res = max(res, total / cnt)
        return total, cnt
    dfs(root)
    return res

if __name__ == '__main__':
    
    #  Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

    # A subtree of a tree is any node of that tree plus all its descendants.

    # The average value of a tree is the sum of its values, divided by the number of nodes.

    

    # Example 1:


    # Input: root = [5,6,1]
    # Output: 6.00000
    # Explanation: 
    # For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
    # For the node with value = 6 we have an average of 6 / 1 = 6.
    # For the node with value = 1 we have an average of 1 / 1 = 1.
    # So the answer is 6 which is the maximum.
    # Example 2:

    # Input: root = [0,null,1]
    # Output: 1.00000
    

    # Constraints:

    # The number of nodes in the tree is in the range [1, 104].
    # 0 <= Node.val <= 105

    root = TreeNode(5,TreeNode(6),TreeNode(1))
    print(maximumAverageSubtree(root))
    root = TreeNode(0,None,TreeNode(1))
    print(maximumAverageSubtree(root))
