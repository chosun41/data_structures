class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    def dfs(root):
        if not root:
            return 
        res.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    res = []
    dfs(root)
    return ",".join(res)

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    lst = data.split(",")
    stack = []
    head = None
    for n in lst:
        n = int(n)
        if not head:
            head = TreeNode(n)
            stack.append(head)
        else:
            node = TreeNode(n)
            if n < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < n: 
                    u = stack.pop()
                u.right = node
            stack.append(node)
    return head

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