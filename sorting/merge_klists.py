class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    heap = [(lists[i].val, i) for i in range(len(lists)) if lists[i]]
    heapq.heapify(heap)
    head = None
    while heap:
        nex = heapq.heappop(heap)
        node = ListNode(nex[0])
        index = nex[1]
        if not head:
            head = node
            trav = head
        else:
            trav.next = node
            trav = trav.next
        if lists[index].next:
            lists[index] = lists[index].next
            heapq.heappush(heap, (lists[index].val, index))
    return head 

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
    
        
        