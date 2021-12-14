class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def remove_duplicates(L):

    it = L
    
    while it:
        
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        
        # just keep reattaching next_distinct while data value repeats
        while next_distinct and next_distinct.val == it.val:
            next_distinct = next_distinct.next
            
        it.next = next_distinct
        
        it = it.next
     
    # return list amended
    return L

if __name__ == "__main__":
    
    # naive: hash table while traversing
    # time: O(n)
    # space: O(1)
   
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(2)
    l1.next.next.next=ListNode(3)
    l1.next.next.next.next=ListNode(4)
    l1.next.next.next.next.next=ListNode(4)
    l1.next.next.next.next.next.next=ListNode(4)
    l1.next.next.next.next.next.next.next=ListNode(5)

    x=remove_duplicates(l1)
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
