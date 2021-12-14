class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def sumNumbers(root):
    root_to_leaf = 0
    stack = [(root, 0) ]
    
    while stack:
        root, curr_number = stack.pop()
        if root: # if node
            curr_number = curr_number * 10 + root.val
            # if it's a leaf, update root-to-leaf sum
            if not root.left and not root.right:
                root_to_leaf += curr_number
            else:
                stack.append((root.right, curr_number)) # append even if none
                stack.append((root.left, curr_number))
                    
    return root_to_leaf

if __name__ == '__main__':

    # You are given the root of a binary tree containing digits from 0 to 9 only.

    # Each root-to-leaf path in the tree represents a number.

    # For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    # Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

    # A leaf node is a node with no children. 12+13 = 25

    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(3)
    print(sumNumbers(x))