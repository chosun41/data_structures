class ListNode:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

# detect if cycle exists
def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow.val

    return None
    
# which node starts the cycle
# find where they meet
# reset slow at head and traverse slow and fast one by one until they meet
# return slow.val
def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow.val


# length of a cycle
# find where they meet
# set slow to slow.next
# increment until it reaches back to fast and record length
def cycle_length(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    slow = slow.next
    length = 1
    while slow!=fast:
        slow = slow.next
        length+=1
    return length

if __name__ == "__main__":

    # time: O(n)
    # space: O(1)
    
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node3
    
    print(has_cycle(node0))
    # s,f
    # 0,0
    # 1,2
    # 2,4
    # 3,6
    # 4,8
    # 5,4
    # 6,6
    
    print("\n")
    print(cycle_start(node0))
    # s,f
    # 1,2
    # 2,4
    # 3,6
    # 4,8
    # 5,4
    # 6,6
    # 0,6
    # 1,7
    # 2,8
    # 3,3
    # 3

    print("\n")
    print(cycle_length(node0))
    
    # cycle start and cycle length both have slow and fast at index 1 and 2 not 0 and 1
        # s,f
    # 1,2
    # 2,4
    # 3,6
    # 4,8
    # 5,4
    # 6,6
    # 0,6
    # looplength -6

    