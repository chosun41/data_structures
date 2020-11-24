from binary_tree import BinaryTree

def printAncestors(root, target): 
      
    # Base case 
    if root == None: 
        return False 
      
    if root.data == target: 
        return True 
  
    # If target is present in either left or right subtree  
    # of this node, then print this node 
    if (printAncestors(root.left, target) or 
        printAncestors(root.right, target)): 
        print(root.data) 
        return True
  
    # Else return False  
    return False
    
if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    printAncestors(root, 7)