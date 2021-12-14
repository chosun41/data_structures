class Node:
    
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

# kill every m person out of a group of size n, who remains
# start from index 0
def getJosephusPosition(n, m):
    
    # create circular linked list
    final_ll=Node()
    curr = final_ll
    
    for x in range(n):
        curr.next = Node(x)
        curr = curr.next

    curr.next = final_ll.next
    curr = curr.next

    # extract items from linked list in proper order
    prev = curr
    counter = 0
    
    while curr.next != curr:
        counter += 1
        if counter % m == 0:
            prev.next = curr.next
            # kill and set prev.next to currentNode.next
        else:
            prev = curr
            # set prev to current node
        curr = curr.next
        # set current to current next
   
    return curr.val
    
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
