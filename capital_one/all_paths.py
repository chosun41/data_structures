from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def binaryTreePaths(root):
    q = deque([(root,[str(root.val)])])
    res = []
    while q:
        node, path = q.popleft()
        if node:
            if not node.left and not node.right:
                res.append('->'.join(path))
            if node.left:
                q.append((node.left,path + [str(node.left.val)]))
            if node.right:
                q.append((node.right, path + [str(node.right.val)]))
    return res

if __name__ == '__main__':
    # time and space: O(n)
    x=TreeNode(1)
    x.left=TreeNode(2)
    x.right=TreeNode(3)
    x.left.right=TreeNode(5)
    print(binaryTreePaths(x))