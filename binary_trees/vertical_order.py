import collections

class TreeNode:
    
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def verticalTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    frontier = [(root, 0)]
    h = collections.defaultdict(list)
    while frontier:
        next = []
        for u, x in frontier:
            h[x].append(u.val)
            if u.left: 
                next.append((u.left, x-1)) 
            if u.right: 
                next.append((u.right, x+1))
            next.sort(key = lambda x: (x[1], x[0].val))
        frontier = next
    for k in sorted(h):
        res.append(h[k])
    return res

def verticalTraversal2(root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

if __name__=='__main__':

    # Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

    # For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

    # The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

    # Return the vertical order traversal of the binary tree.

    # left to right, order based on y coordinate
    # time: O(nlogn)
    # space: O(n)
    x=TreeNode(3)
    x.left=TreeNode(9)
    x.right=TreeNode(20)
    x.right.left=TreeNode(15)
    x.right.right=TreeNode(7)
    print(verticalTraversal(x))
    print(verticalTraversal2(x))
    
    y=TreeNode(1)
    y.left=TreeNode(2)
    y.right=TreeNode(3)
    y.left.left=TreeNode(4)
    y.left.right=TreeNode(5)
    y.right.left=TreeNode(6)
    y.right.right=TreeNode(7)
    print(verticalTraversal(y))
    print(verticalTraversal2(y))