from copy import deepcopy
from binary_tree import BinaryTree,levelOrder

# mirror flip image

def MirrorOfBinaryTree(root):
    if(root != None):
        MirrorOfBinaryTree(root.left)
        MirrorOfBinaryTree(root.right)

        # swap the pointers in this node
        root.left,root.right=root.right,root.left

    return root

def areMirror(a, b): 
      
    # Base case : Both empty 
    if a is None and b is None: 
        return True
      
    # If only one is empty 
    elif a is None or b is None: 
        return False
      
    # Both non-empty, compare them  
    # recursively. Note that in  
    # recursive calls, we pass left 
    # of one tree and right of other tree 
    return (a.data == b.data and 
            areMirror(a.left, b.right) and 
            areMirror(a.right,b.left)) 

            
if __name__ == '__main__':
    
    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.insertRight(3)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    root1.getRight().insertLeft(6)
    root1.getRight().insertRight(7)
    print(levelOrder(root1,[]))
    
    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    mirror_root = MirrorOfBinaryTree(deepcopy(root1))
    print(levelOrder(mirror_root,[]))
    
    print(areMirror(root1, mirror_root))

    