class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def treeToDoublyList(root):
    def dfs(node):
        """
        Performs standard inorder traversal:
        left -> node -> right
        and links all nodes into DLL
        """
        nonlocal head, tail
        if not node:
            return

        # left
        dfs(node.left)
        # node 
        if tail:
            # link the previous node (last)
            # with the current one (node)
            tail.right = node
            node.left = tail
        else:
            # keep the smallest node
            # to close DLL later on
            head = node        
        tail = node
        # right
        dfs(node.right)

    # the smallest (first) and the largest (last) nodes
    head, tail = None, None
    dfs(root)
    # close DLL
    head.left = tail
    tail.right = head
    return head

if __name__=='__main__':
    
    # left and right are like predecessor and succesor
    # nodes are listed in inorder traversal order
    x=Node(4)
    x.left=Node(2)
    x.right=Node(5)
    x.left.left=Node(1)
    x.left.right=Node(3)
    #    4
    #  2 5
    # 1 3
    y=treeToDoublyList(x)
    print(y.val)
    print(y.right.val)
    print(y.right.right.val)
    print(y.right.right.right.val)
    print(y.right.right.right.right.val)
    print(y.right.right.right.right.left.val)