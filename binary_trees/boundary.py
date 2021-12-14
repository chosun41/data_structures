class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# nodes around the exterior of binary tree

exterior = []

def leaves(root): 
    if(root): 
        leaves(root.left) 
          
        # Print it if it is a leaf node 
        if root.left is None and root.right is None: 
            exterior.append(root.val) 
  
        leaves(root.right)

# A function to print all left boundary nodes, except a  
# leaf node. Print the nodes in TOP DOWN manner 
def boundary_left(root): 
      
    if(root): 
        if (root.left): 
              
            # to ensure top down order, print the node 
            # before calling itself for left subtree 
            exterior.append(root.val) 
            boundary_left(root.left) 
          
        elif(root.right): 
            exterior.append(root.val) 
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
            exterior.append(root.val) 
          
        elif(root.left): 
            boundary_right(root.left) 
            exterior.append(root.val) 
  
        # do nothing if it is a leaf node, this way we  
        # avoid duplicates in output 
  
  
# A function to do boundary traversal of a given binary tree 
def boundary(root): 
    
    if (root): 
        
        exterior.append(root.val)
          
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

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    print(boundary(root))
    
    #                 1
    #            2         3
    #         4    5    6     7
    #       8 9 10 11 12 13 14 15