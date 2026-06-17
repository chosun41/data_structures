class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # If the main tree is empty, it cannot contain any non-empty subtree
        if not root:
            return False

        # 1. Check if the trees rooted at the current nodes match perfectly
        if self.isSameTree(root, subRoot):
            return True

        # 2. If they don't match, look for subRoot in the left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are null, they are identical
        if not p and not q:
            return True
        # If only one node is null, or their values don't match, they are not identical
        if not p or not q or p.val != q.val:
            return False

        # Recursively check if left subtrees and right subtrees match perfectly
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":

    # Helper function to easily construct a tree from a list (Level-order / BFS input)
    def build_tree(elements):
        if not elements:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in elements]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    sol = Solution()

    # --- Test Case 1: True Match ---
    # Main Tree:      3          SubRoot Tree:    4
    #               /   \                       /   \
    #              4     5                     1     2
    #            /   \
    #           1     2
    root1 = build_tree([3, 4, 5, 1, 2])
    subRoot1 = build_tree([4, 1, 2])

    print("Test Case 1 Result:", sol.isSubtree(root1, subRoot1))  # Expected output: True

    # --- Test Case 2: False Match (Extra child node) ---
    # Main Tree:      3          SubRoot Tree:    4
    #               /   \                       /   \
    #              4     5                     1     2
    #            /   \
    #           1     2
    #                /
    #               0
    root2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot2 = build_tree([4, 1, 2])

    print("Test Case 2 Result:", sol.isSubtree(root2, subRoot2))  # Expected output: Fals