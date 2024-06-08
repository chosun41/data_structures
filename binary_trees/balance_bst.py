class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def balanceBST(root):
    vals=[]
    def inorder(node):
        if node:
            inorder(node.left)
            vals.append(node)
            inorder(node.right)
    def balance(l, r):
        if l<=r:
            mid = (l+r)//2
            cur = vals[mid]
            cur.left = balance(l, mid-1)
            cur.right = balance(mid+1, r)
            return cur
    inorder(root)
    n=len(vals)

    return balance(0, n-1)

if __name__ == '__main__':

    # time: O(n)
    # space: O(1)

    x = TreeNode(1)
    x.right = TreeNode(2)
    x.right.right = TreeNode(3)
    x.right.right.right = TreeNode(4)

    y = balanceBST(x)
    print(y.val)
    print(y.left.val)
    print(y.right.val)
    print(y.right.right.val)