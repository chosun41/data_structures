class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root):
    def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]

if __name__=='__main__':
    # find largest bst subtree with num of nodes in it
    # time: O(n)
    # height: O(h) h height of tree
    
    x=TreeNode(10)
    x.left=TreeNode(5)
    x.right=TreeNode(15)
    x.left.left=TreeNode(1)
    x.left.right=TreeNode(8)
    x.right.right=TreeNode(7)
    print(largestBSTSubtree(x))
    