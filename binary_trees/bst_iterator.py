
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BSTIterator:
    
    def __init__(self, root: TreeNode):

        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest element in the BST
        self.index = -1

        # Call to flatten the input binary search tree
        self._inorder(root)
        self.length = len(self.nodes_sorted)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        if self.index >= self.length:
            return -1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < self.length

if __name__ == '__main__':

    # Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    # BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    # boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    # int next() Moves the pointer to the right, then returns the number at the pointer.
    # Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

    # You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

    # time and space: O(n)

    x = TreeNode(7)
    x.left = TreeNode(3)
    x.right = TreeNode(15)
    x.right.left = TreeNode(9)
    x.right.right = TreeNode(20)
    #   7
    # 3   15
    #    9  20
    bSTIterator = BSTIterator(x)
    print(bSTIterator.next());    # return 3
    print(bSTIterator.next());    # return 7
    print(bSTIterator.hasNext()); # return True
    print(bSTIterator.next());    # return 9
    print(bSTIterator.hasNext()); # return True
    print(bSTIterator.next());    # return 15
    print(bSTIterator.hasNext()); # return True
    print(bSTIterator.next());    # return 20
    print(bSTIterator.hasNext()); # return False
    print(bSTIterator.next());