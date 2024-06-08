from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def serialize(root):
    """Encodes a tree to a single string.
    """
    if not root: return ''
    tree = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            tree.append(str(node.val))
            queue.extend([node.left, node.right])
        else:
            tree.append('*')
    return ','.join(tree)
    

def deserialize(data):
    """Decodes your encoded data to tree.
    """
    if not data: return None
    tree = deque(data.split(','))
    root = TreeNode(int(tree.popleft()))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        
        if (left := tree.popleft()) != '*':
            node.left = TreeNode(int(left))
            queue.append(node.left)
        
        if (right := tree.popleft()) != '*':
            node.right = TreeNode(int(right))
            queue.append(node.right)
            
    return root

if __name__=='__main__':
    # time: O(n) for both
    x=TreeNode(2)
    x.left=TreeNode(1)
    x.left.left=TreeNode(0)
    x.right=TreeNode(3)
    x.right.right=TreeNode(4)
    y=serialize(x)
    print(y)
    z=deserialize(y)
    print(z.right.val)
    print(z.right.right.val)