class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def pathFinder(root, val, path, paths):
    if not root:
        return False
    
    # when you reached the leaves
    if not root.left and not root.right:
        if root.val == val: # here
            path.append(root.val)
            paths.append(path)
            return True
        else:
            return False
    
    left = pathFinder(root.left, val - root.val, path + [root.val], paths)
    right = pathFinder(root.right, val - root.val, path + [root.val], paths)  # make sure it can be executed!
    return left or right

def hasPathWithSum(root, val):
    paths = []
    pathFinder(root, val, [], paths)
    print('sum:', val)
    print('paths:', paths)

if __name__ == '__main__':
    
    # find a path from root to leaf in binary tree which has indicated sum
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    
    hasPathWithSum(root1, 4)
    hasPathWithSum(root1, 11)
    hasPathWithSum(root1, 8)