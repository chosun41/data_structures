class TreeNode():

    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def maxProduct(root):
    res = total = 0

    def s(root):
        nonlocal res
        if not root: return 0
        left, right = s(root.left), s(root.right)
        res = max(res, left * (total - left), right * (total - right))
        return left + right + root.val

    total = s(root)
    s(root)
    return res % (10**9 + 7)

if __name__ == '__main__':
    
    # Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

    # Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

    # Note that you need to maximize the answer before taking the mod and not after taking it.

    

    # Example 1:


    # Input: root = [1,2,3,4,5,6]
    # Output: 110
    # Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
    # Example 2:


    # Input: root = [1,null,2,3,4,null,null,5,6]
    # Output: 90
    # Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
    # Example 3:

    # Input: root = [2,3,9,10,7,8,6,5,4,11,1]
    # Output: 1025
    # Example 4:

    # Input: root = [1,1]
    # Output: 1
    

    # Constraints:

    # The number of nodes in the tree is in the range [2, 5 * 104].
    # 1 <= Node.val <= 104

    x = TreeNode(1)
    x.left = TreeNode(2,TreeNode(4),TreeNode(5))
    x.right = TreeNode(3,None,TreeNode(6))

    print(maxProduct(x))