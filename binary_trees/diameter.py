class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# diameter is the number of nodes along the longest path b/t any two nodes 
# basically get the max height from left and right

def diameter(root):
    diameter = 0

    def longest_path(node):
        if not node:
            return 0
        nonlocal diameter
        # recursively find the longest path in
        # both left child and right child
        left_path = longest_path(node.left)
        right_path = longest_path(node.right)

        # update the diameter if left_path plus right_path is larger
        diameter = max(diameter, left_path + right_path) # diameter is b/t any two nodes even through the root along the way

        # return the longest one between left_path and right_path;
        # remember to add 1 for the path connecting the node and its parent
        return max(left_path, right_path) + 1

    longest_path(root)
    return diameter

if __name__ == '__main__':
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print(diameter(root))
    # print(height(root))
