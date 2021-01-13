from lll import LinkedList,Node

# detect if cycle exists
def has_cycle(L1):

    # start at same place
    fast = slow = L1.head
    
    while fast and fast.next:
        
        # increment by 1 and 2, eventually they will meet if they have a cycle
        slow, fast = slow.next, fast.next.next
        print(f"current slow is {slow.data}")
        print(f"current fast is {fast.data}")
        
        if slow is fast:
            
            return slow.data
            
    return None

# which node starts the cycle
def cycle_start(L1):

    if L1.head == None or L1.head.next == None:
        return None

    slow = L1.head.next
    fast = slow.next

    # first make sure slow and fast meet, this will not necessarily be the cycle start
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    # start from the head and increment both slow and fast by 1
    # the distance from head to cycle start = current fast to end of cycle
    slow = L1.head # traverse from beginning
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow.get_data()  # beginning of loop

# length of a cycle
def cycle_length(L1):
                 
    if L1.head == None or L1.head.next == None:
        return 0

    slow = L1.head.next
    fast = slow.next
    
    # first make sure slow and fast meet, this will not necessarily be the cycle start
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    # start a counter at 1
    # set slow to next so it doesnt conflict with while condition
    # traverse and increment counter until you come back to stationary fast
    loopLength = 1
    slow = slow.next # traverse from meeting point

    while slow != fast:
        slow = slow.next
        loopLength += 1
                 
    return loopLength


if __name__ == "__main__":

    # time: O(n)
    # space: O(1)
    
    l1 = LinkedList()
    
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node3

    l1.head = node0
    
    print(has_cycle(l1))
    
    print("\n")
    print(cycle_start(l1))

    print("\n")
    print(cycle_length(l1))
    
    # cycle start and cycle length both have slow and fast at index 1 and 2 not 0 and 1

    