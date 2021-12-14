class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def lca(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    def recurse_tree(current_node):

        nonlocal ans

        # If reached the end of a branch, return False.
        if not current_node:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)

        # Right Recursion
        right = recurse_tree(current_node.right)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q # most important

        # If any two of the three flags left, right or mid become True. current_node is the lca
        if mid + left + right >= 2:
            ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    ans = None
    recurse_tree(root)
    return ans

if __name__ == '__main__':

    # time and space: O(n)
    
    # least common ancestor (most recent) of regular binary tree

    # Start traversing the tree from the root node.
    # If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
    # If either of the left or the right branch returns True, this means one of the two nodes was found below.
    # If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.
    # return True via backtrack up to ancestor if left

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    
    #    1
    #  2   3
    # 4 5 6 7
    
    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    print(lca(root1, root1.left.left, root1.left.right).val)
    # print(lca(root1, 4, 5).val)
    # print(lca(root1, 2, 3).val)
    print(lca(root1, root1.left, root1.right.left).val)