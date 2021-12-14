class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque

def rightSideView(root):
    if not root:
        return []
    
    next_level = deque([root])
    rightside = []
    
    while next_level:
        # prepare for the next level
        curr_level = next_level
        next_level = deque()

        while curr_level:
            node = curr_level.popleft()
                
            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        # The current level is finished.
        # Its last element is the rightmost one.
        rightside.append(node.val)
    
    return rightside

if __name__ == '__main__':

    # time: O(n)
    # space: O(d) d-diameter

    x = TreeNode(1)
    x.left = TreeNode(2)
    x.left.right = TreeNode(5)
    x.right = TreeNode(3)
    print(rightSideView(x))