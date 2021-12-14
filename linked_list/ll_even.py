class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def isLinkedListLengthEven(L1):
    current = L1

    while current and current.next:

        current = current.next.next

    if not current:
        return True
    return False
        
if __name__ == "__main__":

    # using only a fast pointer
    # if even, then current pointer is none, else it will have data
    # time: O(n)
    # space: O(1)
    
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(3)
    l1.next.next.next=ListNode(4)
    l1.next.next.next.next=ListNode(5)

    print(isLinkedListLengthEven(l1))