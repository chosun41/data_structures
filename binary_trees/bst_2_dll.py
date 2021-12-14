class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def treeToDoublyList(root):
    def helper(node):
        """
        Performs standard inorder traversal:
        left -> node -> right
        and links all nodes into DLL
        """
        nonlocal last, first
        if node:
            # left
            helper(node.left)
            # node 
            if last:
                # link the previous node (last)
                # with the current one (node)
                last.right = node
                node.left = last
            else:
                # keep the smallest node
                # to close DLL later on
                first = node        
            last = node
            # right
            helper(node.right)

    if not root:
        return None

    # the smallest (first) and the largest (last) nodes
    first, last = None, None
    helper(root)
    # close DLL
    last.right = first
    first.left = last
    return first

if __name__=='__main__':
    
    # left and right are like predecessor and succesor
    # nodes are listed in inorder traversal order
    x=Node(4)
    x.left=Node(2)
    x.right=Node(5)
    x.left.left=Node(1)
    x.left.right=Node(3)
    y=treeToDoublyList(x)
    print(y.val)
    print(y.right.val)
    print(y.right.right.val)
    print(y.right.right.right.val)
    print(y.right.right.right.right.val)
    print(y.right.right.right.right.right.val)