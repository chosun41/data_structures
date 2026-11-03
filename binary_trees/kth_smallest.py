class TreeNode():
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    stack = []
    
    while True:
        # append lefts to stk
        while root:
            stack.append(root)
            root = root.left
        # pop and decrement k
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        # check if anything on the right
        root = root.right

if __name__ == '__main__':

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:
    x = TreeNode(3)
    x.left = TreeNode(1)
    x.right = TreeNode(4)
    x.left.right = TreeNode(2)
    print(kthSmallest(x, 1))

# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

    x = TreeNode(5)
    x.left = TreeNode(3)
    x.right = TreeNode(6)
    x.left.right = TreeNode(4)
    x.left.left = TreeNode(2)
    x.left.left.left = TreeNode(1)
    print(kthSmallest(x, 3))


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3