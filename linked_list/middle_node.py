class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def findMiddleNode(L1):
    
    fast = L1
    slow = L1

    while fast:
        fast = fast.next
        if not fast:
            return slow.val

        fast = fast.next   
        slow = slow.next
        
    return slow.val
    
if __name__ == "__main__":

    # by the time fast pointer reaches end, the slow pointer will be at the middle pointer
    # odd then median numbered node, even then n/2+1 node
    # time: O(n)
    # space: O(1)
    
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    l1.next.next.next.next=ListNode(5)

    print(findMiddleNode(l1))