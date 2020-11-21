from cll import LinkedList,Node

def getJosephusPosition(n, m):
    
    # create circular linked list
    final_ll=LinkedList()
    
    for x in range(n):
        final_ll.addNode(Node(x))

    # extract items from linked list in proper order
    currentNode = prev = final_ll.head
    counter = 0
    
    while currentNode.get_next() != currentNode:
        counter += 1
        if counter % m == 0:
            prev.set_next(currentNode.next)
            # kill and set prev.next to currentNode.next
        else:
            prev = currentNode
            # set prev to current node
        currentNode = currentNode.get_next()
        # set current to current next
   
    return currentNode.get_data()
    
if __name__ == "__main__":
    
    # first index is 0, last survivor is return
    # time: O(n)
    # space: O(1)
    
    print("\n")
    print(getJosephusPosition(6,3))
    
    # 012345 
    # 01345 - kill 2
    # 0134 - kill 5
    # 014 - kill 3
    # 04 - kill 1
    # 0 - kill 4
