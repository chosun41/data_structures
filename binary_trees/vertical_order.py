import collections

class TreeNode:
    
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def verticalTraversal2(root):
    cols = collections.defaultdict(list)
    q = collections.deque([(root,0)])

    while q:
        node, i = q.popleft()
        cols[i].append(node.val)
        if node.left:
            q.append((node.left, i-1))
        if node.right:
            q.append((node.right,i+1))
    return [cols[key] for key in sorted(cols.keys())]

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
    print(verticalTraversal2(x))
    #   3
    #  9  20
    #    15 7
    
    y=TreeNode(1)
    y.left=TreeNode(2)
    y.right=TreeNode(3)
    y.left.left=TreeNode(4)
    y.left.right=TreeNode(5)
    y.right.left=TreeNode(6)
    y.right.right=TreeNode(7)
    print(verticalTraversal2(y))
    #    1
    #  2   3
    # 4 5 6 7