from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def sumNumbers(root):
    
    q = deque([(root,0)])
    res = 0
    while q:
        node, summ = q.popleft()
        if node:
            summ = summ*10 + int(node.val)
            if not node.left and not node.right:
                res+=summ
            if node.left:
                q.append((node.left, summ))
            if node.right:
                q.append((node.right, summ))
    return res

if __name__ == '__main__':

    # You are given the root of a binary tree containing digits from 0 to 9 only.

    # Each root-to-leaf path in the tree represents a number.

    # For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
    # Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

    # A leaf node is a node with no children. 12+13 = 25

    x = TreeNode(1)
    x.left = TreeNode(2)
    x.right = TreeNode(3)
    print(sumNumbers(x))