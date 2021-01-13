from binary_tree import BinaryTree

# nodes around the exterior of binary tree

exterior = []

def leaves(root): 
    if(root): 
        leaves(root.left) 
          
        # Print it if it is a leaf node 
        if root.left is None and root.right is None: 
            exterior.append(root.data) 
  
        leaves(root.right)

# A function to print all left boundary nodes, except a  
# leaf node. Print the nodes in TOP DOWN manner 
def boundary_left(root): 
      
    if(root): 
        if (root.left): 
              
            # to ensure top down order, print the node 
            # before calling itself for left subtree 
            exterior.append(root.data) 
            boundary_left(root.left) 
          
        elif(root.right): 
            exterior.append(root.data) 
            boundary_left(root.right) 
          
        # do nothing if it is a leaf node, this way we 
        # avoid duplicates in output 
  
  
# A function to print all right boundary nodes, except 
# a leaf node. Print the nodes in BOTTOM UP manner 
def boundary_right(root): 
      
    if(root): 
        if (root.right): 
            # to ensure bottom up order, first call for 
            # right subtree, then print this node 
            boundary_right(root.right) 
            exterior.append(root.data) 
          
        elif(root.left): 
            boundary_right(root.left) 
            exterior.append(root.data) 
  
        # do nothing if it is a leaf node, this way we  
        # avoid duplicates in output 
  
  
# A function to do boundary traversal of a given binary tree 
def boundary(root): 
    
    if (root): 
        
        exterior.append(root.data)
          
        # Print the left boundary in top-down manner 
        boundary_left(root.left) 
  
        # Print all leaf nodes 
        leaves(root.left) 
        leaves(root.right) 
  
        # Print the right boundary in bottom-up manner 
        boundary_right(root.right) 
        
    return exterior
  
if __name__ == '__main__':
    
    # 5 pieces - root, left boundary, left leaves, right leaves, right boundary

    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    root.getLeft().getLeft().insertLeft(8)
    root.getLeft().getLeft().insertRight(9)
    root.getLeft().getRight().insertLeft(10)
    root.getLeft().getRight().insertRight(11)
    root.getRight().getLeft().insertLeft(12)
    root.getRight().getLeft().insertRight(13)
    root.getRight().getRight().insertLeft(14)
    root.getRight().getRight().insertRight(15)
    print(boundary(root))
    
    #                 1
    #            2         3
    #         4    5    6     7
    #       8 9 10 11 12 13 14 15