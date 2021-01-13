# complete is right and left subtrees differ by at most 1 height and all the way to the left
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def isCompleteTree(root):
    nodes = [(root, 1)]
    i = 0
    while i < len(nodes):
        node, v = nodes[i]
        i += 1
        if node:
            nodes.append((node.left, 2*v))
            nodes.append((node.right, 2*v+1))

    return  nodes[-1][1] == len(nodes)
    
if __name__=='__main__':
    # time and space: O(n)
    x=TreeNode(1)
    x.left=TreeNode(2)
    x.right=TreeNode(3)
    x.left.left=TreeNode(4)
    x.left.right=TreeNode(5)
    x.right.left=TreeNode(6)
    print(isCompleteTree(x))
    y=TreeNode(1)
    y.left=TreeNode(2)
    y.right=TreeNode(3)
    y.left.left=TreeNode(4)
    y.left.right=TreeNode(5)
    y.right.right=TreeNode(7)
    print(isCompleteTree(y))    
   