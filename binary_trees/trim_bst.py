from bst import BST,levelOrder
from copy import deepcopy

# trim bst in b/t min and max values

def trimBST(root, minVal, maxVal): 
    
    if not root: 
        return 
    root.setLeft(trimBST(root.getLeft(), minVal, maxVal)) 
    root.setRight(trimBST(root.getRight(), minVal, maxVal)) 
    
    if minVal <= root.get_data() <= maxVal: 
        return root 
    if root.get_data() < minVal: 
        return root.getRight() 
    if root.get_data() > maxVal: 
        return root.getLeft()
    
if __name__ == '__main__':
    
    root2 = BST(4)
    root2.insert(2)
    root2.insert(1)
    root2.insert(3)
    root2.insert(6)
    root2.insert(5)
    root2.insert(7)
    
    #      4
    #   2    6
    # 1  3 5   7
    
    x=trimBST(deepcopy(root2),2,6)
    print(levelOrder(x, []))
    
    y=trimBST(deepcopy(root2),3,5)
    print(levelOrder(y, []))
    
    a=trimBST(deepcopy(root2),1,6)
    print(levelOrder(a, []))
    
    b=trimBST(deepcopy(root2),2,7)
    print(levelOrder(b, []))