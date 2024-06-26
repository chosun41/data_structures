class Node:

    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
        
def insert(head, insertVal):

    if not head:
        newNode = Node(insertVal)
        newNode.next = newNode
        return newNode

    prev, curr = head, head.next
    toInsert = False

    while True: # all in while TRUE

        if prev.val <= insertVal <= curr.val:
            # Case #1.
            toInsert = True
        elif prev.val > curr.val: # ex. 1,2,3,4 prev=4,curr=1 !!! most important
            # Case #2. where we locate the tail element
            # 'prev' points to the tail, i.e. the largest element!
            if insertVal >= prev.val or insertVal <= curr.val:
                toInsert = True

        if toInsert:
            prev.next = Node(insertVal, curr)
            # mission accomplished
            return head

        prev, curr = curr, curr.next
        # this conditional afterwards
        if prev == head:
            break
    # Case #3.
    # did not insert the node in the loop
    # prev.next = Node(insertVal, curr)
    return head
    
if __name__ == '__main__':
    # time: O(n)
    # space: O(1)
    x=Node(3)
    x.next=Node(4)
    x.next.next=Node(1)
    x.next.next.next=x
    y=insert(x,2)
    print(y.next.next.next.val)
    print(y.next.next.next.next.val)

    # 3-4-1, insertVal=2
    # prev, head, toInsert - 3,4,False
    # prev, head, toInsert - 4,1,False
    # prev, head, toInsert - 1,3,True 1<=2<=3

    x=Node(3)
    x.next=Node(4)
    x.next.next=Node(1)
    x.next.next.next=x
    y=insert(x,5)
    print(y.next.next.val)
    print(y.next.next.next.val)