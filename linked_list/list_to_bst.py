class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def findSize(head):
    ptr = head
    c = 0
    while ptr:
        ptr = ptr.next
        c += 1
    return c

def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """

    # Get the size of the linked list first
    size = findSize(head)

    # Recursively form a BST out of linked list from l --> r
    def convert(l, r):
        nonlocal head

        # Invalid case
        if l > r:
            return None

        mid = (l + r) // 2

        # First step of simulated inorder traversal. Recursively form
        # the left half
        left = convert(l, mid - 1)

        # Once left half is traversed, process the current node
        node = TreeNode(head.val)   
        node.left = left

        # Maintain the invariance mentioned in the algorithm
        head = head.next

        # Recurse on the right hand side and form BST out of them
        node.right = convert(mid + 1, r)
        return node
    return convert(0, size - 1)

if __name__=='__main__':
    # time: O(n)
    # space: O(logn)
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