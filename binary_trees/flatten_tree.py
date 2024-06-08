class TreeNode:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None
        
def flatten(root):

    def dfs(node): 
        if node.right: 
            dfs(node.right)
        if node.left:
            dfs(node.left)
        right = node.right
        node.left, node.right = None, node.left
        while node.right: 
            node = node.right
        node.right = right
    if root: 
        dfs(root)
    return root
        
if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # flatten a tree into a right leaning tree (linked list)
    x=TreeNode(1)
    x.left=TreeNode(2)
    x.right=TreeNode(5)
    x.left.left=TreeNode(3)
    x.left.right=TreeNode(4)
    x.right.right=TreeNode(6)
    #   1
    #  2  5
    # 3 4  6
    y=flatten(x)
    print(y.val)
    print(y.right.val)
    print(y.right.right.val)
    print(y.right.right.right.val)
    print(y.right.right.right.right.val)
    
