from binary_tree import BinaryTree

def IsBST(root, min, max):
    
    # shrinking min and max with each recursive calls
    
    # reached end
    if root == None:
        return True
    # outside of min and max bounds
    if root.data <= min or root.data >= max:
        return False
    # min < root.left < root
    result = IsBST(root.left, min, root.data)
    # root < root.right < max
    result = result and IsBST(root.right, root.data, max)
    
    return result

if __name__ == '__main__':
    
    # time: O(n)
    # space: O(n)

    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.insertRight(3)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    root1.getRight().insertLeft(6)
    root1.getRight().insertRight(7)
    
    #    1
    #  2   3
    # 4 5 6 7
    
    print(IsBST(root1,-float("infinity"),float("infinity")))
    
    root2 = BinaryTree(4)
    root2.insertLeft(2)
    root2.insertRight(6)
    root2.getLeft().insertLeft(1)
    root2.getLeft().insertRight(3)
    root2.getRight().insertLeft(5)
    root2.getRight().insertRight(7)
    
    #      4
    #   2    6
    # 1  3 5   7
    
    print(IsBST(root2,-float("infinity"),float("infinity")))