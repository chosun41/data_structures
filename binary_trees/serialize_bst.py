from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def serialize(root):

    if not root:
        return ''

    res = []
    current_layer = [root]
    while current_layer:
        new_layer = []
        has_value = False
        for node in current_layer:
            if node != "*":
                res.append(str(node.val))
                if node.left:
                    has_value=True
                    new_layer.append(node.left)
                else:
                    new_layer.append("*")
                if node.right:
                    has_value=True
                    new_layer.append(node.right)
                else:
                    new_layer.append("*")
            else:
                res.append("*")
        current_layer = new_layer if has_value else []


    return ','.join(res)
    

def deserialize(data):
    inp = data.split(",")
    root = TreeNode(inp[0])
    current_level = [root]
    i=1
    while current_level and i<len(inp):
        new_level = []
        for node in current_level:
            if inp[i]!="*":
                node.left = TreeNode(inp[i])
                new_level.append(node.left)
            i+=1
            if inp[i]!="*":
                node.right = TreeNode(inp[i])
                new_level.append(node.right)
            i+=1
        current_level = new_level
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