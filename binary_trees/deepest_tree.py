
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def subtreeWithAllDeepest(root):
    
    # --------------------------------------------
    def helper(node):
        
        # first return item is depth
        # second return item is root of smallest subtree with deepest nooes
        
        if not node:
        
            # base case
            # empty node or empty tree
            return 0, None
        
        l_depth, l_node = helper(node.left)
        r_depth, r_node = helper(node.right)
        
        if l_depth > r_depth:
        
            # left subtree is deeper
            return l_depth+1, l_node
        
        elif r_depth > l_depth:
        
            # right subtree is deeper
            return r_depth+1, r_node
        
        else:
        
            # both subtrees are the same
            # current node is the root of smallest subtree with deepest nodes
            return l_depth+1, node
        
    # --------------------------------------------
    
    # second return item is the answer
    return helper(root)[1]

if __name__=='__main__':

    # find deepest node and return its subtree
    # time and space: O(n)

    x = TreeNode(3)
    x.left = TreeNode(5)
    x.right = TreeNode(1)
    x.left.left=TreeNode(6)
    x.left.right = TreeNode(2)
    x.left.right.left = TreeNode(7)
    x.left.right.right = TreeNode(4)
    x.right.left = TreeNode(0)
    x.right.right = TreeNode(8)

    y = subtreeWithAllDeepest(x)
    print(y.val)
    print(y.left.val)
    print(y.right.val)
