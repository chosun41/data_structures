class TreeNode:

    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def closestValue(root, target):
    closest = root.val
    while root:
        closest = min(root.val, closest, key = lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest
    
if __name__=='__main__':
    # time: O(h) - height of tree
    # space: O(1)
    x=TreeNode(4)
    x.left=TreeNode(2)
    x.right=TreeNode(5)
    x.left.left=TreeNode(1)
    x.left.right=TreeNode(3)
    print(closestValue(x,3.714286))