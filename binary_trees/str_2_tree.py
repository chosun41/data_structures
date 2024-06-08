class TreeNode:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
        
def str2tree(s):
    stack, num = [TreeNode()], ''
    s += '('
    for i, c in enumerate(s):
        if c == ')':
            stack.pop()
        elif c != '(':
            num += c
            if not s[i+1].isdigit():
                node = TreeNode(int(num))
                if stack[-1].left: # find place to attach node to left or right
                    stack[-1].right = node
                else:
                    stack[-1].left = node # everything usually becomes a left of stack top
                stack.append(node) # append node and also attach node to stack -1, two different entries
                num = ''
    return stack[0].left

if __name__ == '__main__':
    # time: O(n)
    x=str2tree("-4(2(3)(1))(6(5)(7))")
    print(x.val)
    print(x.left.val)
    print(x.right.val)

    #   -4
    #  2   6
    # 3 1 5 7