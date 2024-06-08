class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists(lists):
    head = ListNode(None)
    curr = head
    h = []
    # just put on first nodes and set them to next
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    while h:
        val, i = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    return head.next

if __name__ =='__main__':
    
    # time: O(nlogk) for heap k number of linked lists
    # space: O(n) - n # of total nodes
    
    a=ListNode(1)
    a.next=ListNode(4)
    a.next.next=ListNode(5)
    
    b=ListNode(1)
    b.next=ListNode(3)
    b.next.next=ListNode(4)
    
    c=ListNode(2)
    c.next=ListNode(6)
    
    x=mergeKLists([a,b,c])
    print(x.val)
    print(x.next.val)
    print(x.next.next.val)
    print(x.next.next.next.val)
    print(x.next.next.next.next.val)
    
        
        