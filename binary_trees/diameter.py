class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# diameter is the number of nodes along the longest path b/t any two nodes 
# basically get the max height from left and right

def diameter(root):
    diameter = 0

    def dfs(node):
        if not node:
            return 0
        nonlocal diameter
        # recursively find the longest path in
        # both left child and right child
        left_height = dfs(node.left)
        right_height = dfs(node.right)

        # update the diameter if left_path plus right_path is larger
        diameter = max(diameter, left_height + right_height) # diameter is b/t any two nodes even through the root along the way

        # return the longest one between left_path and right_path;
        # remember to add 1 for the path connecting the node and its parent
        return max(left_height, right_height) + 1

    dfs(root)
    return diameter

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # diameter is number of lengths in b/t nodes, not number of nodes along path
    
    print(diameter(root))
    # print(height(root))
