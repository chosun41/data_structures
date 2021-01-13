class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def str2tree(s):
    """
    :type s: str
    :rtype: TreeNode
    """
    if not s:
        return
    stack = []
    num = ""
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == "-":
            num += s[i]    
        elif s[i] == "(":
            if num:
                node = TreeNode(int(num))
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    stack.append(node)
                else:
                    root = node
                    stack.append(node)
                num = ""
        else: # s[i] == ")"
            if num:
                node = TreeNode(int(num))
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                num = ""
            else:
                stack.pop()
    return root if not num else TreeNode(int(num))

if __name__ == '__main__':
    # time: O(n)
    x=str2tree("-4(2(3)(1))(6(5)(7))")
    print(x.val)
    print(x.left.val)
    print(x.right.val)