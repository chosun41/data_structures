class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def rangeSumBST(root, L, R):
    def dfs(node):
        nonlocal ans
        if node:
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)

    ans = 0
    dfs(root)
    return ans

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
    
    print(rangeSumBST(x,7,15))