from binary_tree import BinaryTree

def lca(root, alpha, beta):
    if not root: 
        return None
    if root.data == alpha or root.data == beta: 
        return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)
    if left and right: 
        # alpha & beta are on both sides
        return root
    else: 
        # EITHER alpha/beta is on one side 
        # OR alpha/beta is not in L&R subtrees
        return left if left else right

if __name__ == '__main__':
    
    # least
    
    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.insertRight(3)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    root1.getRight().insertLeft(6)
    root1.getRight().insertRight(7)
    
    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    print(lca(root1, 6, 7).data)
    print(lca(root1, 4, 5).data)
    print(lca(root1, 2, 3).data)
    print(lca(root1, 2, 6).data)