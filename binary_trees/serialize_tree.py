class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def serialize(root):
    if not root:
        return []
    lst, curr_level = [], [root]
    while curr_level:
        next_level, has_value = [], False
        for node in curr_level:
            if node:
                lst.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
                if node.left or node.right:
                    has_value = True
            else:
                lst.append(None)
        curr_level = next_level if has_value else []
    return lst

def deserialize(data):
    n = len(data)
    if n == 0:
        return None
    root = TreeNode(data[0])
    curr_level, i = [root], 1
    while curr_level and i < n:
        next_level = []
        for node in curr_level:
            if data[i]:
                node.left = TreeNode(data[i])
                next_level.append(node.left)
            i += 1
            if data[i]:
                node.right = TreeNode(data[i])
                next_level.append(node.right)
            i += 1
        curr_level = next_level
    return root

if __name__=='__main__':
    x=TreeNode(1)
    x.left=TreeNode(2)
    x.right=TreeNode(3)
    x.right.left=TreeNode(4)
    x.right.right=TreeNode(5)
    y=serialize(x)
    print(y)
    z=deserialize(y)
    print(z.left.val)
    print(z.right.val)