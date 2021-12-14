class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def reorderList(head):
    if not head:
        return 

    # find the middle of linked list [Problem 876]
    # in 1->2->3->4->5->6 find 4 
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 

    # reverse the second part of the list [Problem 206]
    # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
    # reverse the second half in-place
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next       
    
    # 4->None       4,    5         None, 4,5
    # 5->4->None,   5,    6          4,   5, 6
    # 6->5->4->None 6,  None         5,   6,  None

    # merge two sorted linked lists [Problem 21]
    # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
        
    return head
        
if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    # Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    # reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    # 1->2->3->4->5 -? 1->5->2->4->3
    x= ListNode(1)
    x.next=ListNode(2)
    x.next.next=ListNode(3)
    x.next.next.next=ListNode(4)
    x.next.next.next.next=ListNode(5)
    y=reorderList(x)
    print(y.val)
    print(y.next.val)
    print(y.next.next.val)
    print(y.next.next.next.val)
    print(y.next.next.next.next.val)
    