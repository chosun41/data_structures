class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestBSTSubtree(root):
    def dfs(root):
        nonlocal result
        if not root:
            return [True, 0, float('inf'),float('-inf')]
        
        leftIsBST, leftSize, leftMin, leftMax = dfs(root.left)
        rightIsBST, rightSize, rightMin, rightMax = dfs(root.right)

        if leftIsBST and rightIsBST and leftMax<root.val<rightMin:
            result = max(result, leftSize + rightSize + 1)
            leftMin = root.val if leftMin == float('inf') else leftMin
            rightMax = root.val if rightMax == float('inf') else rightMax
            return [True, leftSize + rightSize + 1,leftMin, rightMax]
        else:
            return [False, 0, float('inf'), float('-inf')]


    result = 0
    dfs(root)
    return result

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
    