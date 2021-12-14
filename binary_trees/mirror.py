from copy import deepcopy

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# mirror flip image

def MirrorOfBinaryTree(root):
    if not root:
        return
    MirrorOfBinaryTree(root.left)
    MirrorOfBinaryTree(root.right)

    # swap the pointers in this node
    root.left,root.right=root.right,root.left

    return root

def areMirror(a, b): 
      
    # Base case : Both empty 
    if not a and not b: 
        return True
      
    # If only one is empty 
    elif not a or not b: 
        return False
      
    # Both non-empty, compare them  
    # recursively. Note that in  
    # recursive calls, we pass left 
    # of one tree and right of other tree 
    return (a.val == b.val and 
            areMirror(a.left, b.right) and 
            areMirror(a.right,b.left)) 

            
if __name__ == '__main__':

    # invert binary tree
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)

    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    mirror_root = MirrorOfBinaryTree(deepcopy(root1))
    print(mirror_root.val)
    print(mirror_root.left.val)
    print(mirror_root.right.val)
    print(mirror_root.left.left.val)
    print(mirror_root.right.right.val)
    
    print(areMirror(root1, mirror_root))

    