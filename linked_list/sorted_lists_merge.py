class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def merge_two_sorted_lists(L1,L2):

    # head of both lists
    curr_1 = L1
    curr_2 = L2
    
    # empty linked list
    new_ll = ListNode()
    head = new_ll

    # traverse while still nodes and compare which the least to new_ll
    while curr_1 and curr_2:
        if curr_1.val <= curr_2.val:
            new_ll.next = ListNode(curr_1.val)  
            curr_1 = curr_1.next
        else:
            new_ll.next = ListNode(curr_2.val)
            curr_2=curr_2.next
        new_ll = new_ll.next

    # appends remaining nodes of L1 or L2
    if not curr_1:
        while curr_2:
            new_ll.next = ListNode(curr_2.val)
            curr_2=curr_2.next
            new_ll=new_ll.next
    elif not curr_2:
        while curr_1:
            new_ll.next = ListNode(curr_1.val)
            curr_1 = curr_1.next
            new_ll = new_ll.next
        
    # return the new list
    return head.next

if __name__ == "__main__":
    
    # naive: append everything and sort in place
    # time: O(n+m)
    # space: O(1)
   
    l1 = ListNode(1)
    l2 = ListNode(2)

    l1.next = ListNode(3)
    l2.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2.next.next = ListNode(6)
    l1.next.next.next = ListNode(7)

    x = merge_two_sorted_lists(l1,l2)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
    print(x.next.next.next.next.next.val)
    print(x.next.next.next.next.next.next.val)
    print(x.next.next.next.next.next.next.next.val)