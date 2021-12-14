class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def sortedListToBST(head):
    A, n = [], head
    while n:
        A.append(n.val)
        n = n.next
    def make(i,j):
        if i<=j:
            m       =  (i+j)//2
            n       = TreeNode(A[m])
            n.left  = make(i  ,m-1)
            n.right = make(m+1,j  )
            return n
    return make(0, len(A)-1)

if __name__=='__main__':
    # time: O(n)
    # space: O(n)
    x=ListNode(-10)
    x.next=ListNode(-3)
    x.next.next=ListNode(0)
    x.next.next.next=ListNode(5)
    x.next.next.next.next=ListNode(9)
    y=sortedListToBST(x)
    print(y.val)
    print(y.left.val)
    print(y.right.val)
    print(y.left.right.val)
    print(y.right.right.val)