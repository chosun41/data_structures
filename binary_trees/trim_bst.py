from copy import deepcopy

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# trim bst in b/t min and max values

def trimBST(root, minVal, maxVal): 
    
    if not root: 
        return 
    root.left = trimBST(root.left, minVal, maxVal)
    root.right = trimBST(root.right, minVal, maxVal) 
    
    if minVal <= root.val <= maxVal: 
        return root 
    if root.val < minVal: 
        return root.right
    if root.val > maxVal: 
        return root.left
    
if __name__ == '__main__':
    
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(3)
    root2.right = TreeNode(6)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(7)
    
    #      4
    #   2    6
    # 1  3 5   7
    
    x=trimBST(deepcopy(root2),2,6)
    print(x.val)
    print(x.left.val)
    print(x.right.val)
    print(x.left.left)
    print(x.left.right.val)
    print(x.right.left.val)
    print(x.right.right)
    
    x=trimBST(deepcopy(root2),3,5)
    print(x.val)
    print(x.left.val)
    print(x.right.val)
    
    x=trimBST(deepcopy(root2),1,6)
    print(x.val)
    print(x.left.val)
    print(x.right.val)
    print(x.left.left.val)
    print(x.left.right.val)
    print(x.right.left.val)
    print(x.right.right)
    
    x=trimBST(deepcopy(root2),2,7)
    print(x.val)
    print(x.left.val)
    print(x.right.val)
    print(x.left.left)
    print(x.left.right.val)
    print(x.right.left.val)
    print(x.right.right.val)
 