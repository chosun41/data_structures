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
    # Value of current node or parent node.
    parent_val = root.val

    # Value of p
    p_val = p.val

    # Value of q
    q_val = q.val

    # If both p and q are greater than parent
    if p_val > parent_val and q_val > parent_val:    
        return lca(root.right, p, q)
    # If both p and q are lesser than parent
    elif p_val < parent_val and q_val < parent_val:    
        return lca(root.left, p, q)
    # We have found the split point, i.e. the LCA node.
    else:
        return root

if __name__ == '__main__':

    # time and space: O(n)
    
    # least common ancestor (most recent) of bst

    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(10)
    
    #    6
    #  2   8
    # 1 4 7 10
    
    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    print(lca(root1, root1.left.left, root1.left.right).val)
    # print(lca(root1, 4, 5).val)
    # print(lca(root1, 2, 3).val)
    print(lca(root1, root1.left, root1.right.left).val)