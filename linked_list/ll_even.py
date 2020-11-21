from lll import LinkedList,Node

def isLinkedListLengthEven(L1):
    current = L1.head

    while current != None and current.get_next() != None:
        current = current.get_next().get_next()  

    if current == None:
        return True
    return False
        
if __name__ == "__main__":

    # using only a fast pointer
    # if even, then current pointer is none, else it will have data
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
    print(isLinkedListLengthEven(l1))