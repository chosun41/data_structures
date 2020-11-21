from lll import LinkedList,Node

def findMiddleNode(L1):
    
    fast = L1.head
    slow = L1.head

    while (fast != None):
        fast = fast.get_next()
        if (fast == None):
            return slow.data

        fast = fast.get_next()   
        slow = slow.get_next()
        
    return slow.data
    
if __name__ == "__main__":

    # by the time fast pointer reaches end, the slow pointer will be at the middle pointer
    # odd then median numbered node, even then n/2+1 node
    # time: O(n)
    # space: O(1)
    
    l1 = LinkedList()
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    l1.addNode(node1)
    l1.addNode(node2)
    l1.addNode(node3)
    l1.addNode(node4)
    l1.addNode(node5)

    print("\n")
    print(findMiddleNode(l1))