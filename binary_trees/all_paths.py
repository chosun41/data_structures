class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def binaryTreePaths(root):

    result = []

    def helper(node, cur):

        if not node:
            # base case
            return

        if not node.left and not node.right:
            # stop condition
            result.append( cur + [str(node.val)] )

        else:
            # general case
            helper(node.left, cur + [str(node.val)] )
            helper(node.right, cur + [str(node.val)] )

    helper(node=root, cur=[])
    return [ *map('->'.join, result) ]

if __name__ == '__main__':
    # time and space: O(n)
    x=TreeNode(1)
    x.left=TreeNode(2)
    x.right=TreeNode(3)
    x.left.right=TreeNode(5)
    print(binaryTreePaths(x))