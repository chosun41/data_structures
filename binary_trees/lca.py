from bst import BST
from binary_tree import BinaryTree

# for regular binary tree
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

# for bst - much easier since the bst property of range constricts what can be the lca
def lca2(root, alpha, beta):
    while root:
        if((alpha<=root.data and beta>root.data) or (alpha>root.data and beta<=root.data)):
            return root
        if(alpha<root.data):
            root=root.left
        else:
            root=root.right
    
if __name__ == '__main__':
    
    # least common ancestor (most recent)
    
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
    
    # deep copy since MirrorofBinaryTree will change the original parameter root
    # makes sure that with areMirror function root1 is unchanged
    print(lca(root1, 6, 7).data)
    print(lca(root1, 4, 5).data)
    print(lca(root1, 2, 3).data)
    print(lca(root1, 2, 6).data)
    
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
    
    print(lca2(root2, 5, 7).data)
    print(lca2(root2, 1, 3).data)
    print(lca2(root2, 2, 6).data)
    print(lca2(root2, 2, 5).data)