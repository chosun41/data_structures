from binary_tree import BinaryTree

# may start and end at any node

# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 

globalMax = float("-inf") 

def find_max_sum(root):
    if root is None:
        return 0

    # Recursive calls to children:
    left = find_max_sum(root.left)
    right = find_max_sum(root.right)

    # Max of first three cases:
    return_max = max(max(left, right) + root.data, root.data)

    # Max of all four cases:
    maximum = max(return_max, left + right + root.data)

    # Update globalMax:
    global globalMax
    if maximum > globalMax:
        globalMax = maximum

    return return_max

if __name__ == '__main__':
    
    root = BinaryTree(1)
    root.insertLeft(2)
    root.insertRight(3)
    root.getLeft().insertLeft(4)
    root.getLeft().insertRight(5)
    root.getRight().insertLeft(6)
    root.getRight().insertRight(7)
    
    find_max_sum(root)
    
    print(globalMax)