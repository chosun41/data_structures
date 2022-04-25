
class Node:

    def __init__(self,val=None,next=None,random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head:
        return head

    # Creating a new weaved list of original and copied nodes.
    ptr = head
    while ptr:

        # Cloned node
        new_node = Node(ptr.val, None, None)

        # Inserting the cloned node just next to the original node.
        # If A->B->C is the original linked list,
        # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
        new_node.next = ptr.next
        ptr.next = new_node
        ptr = new_node.next

    ptr = head

    # Now link the random pointers of the new nodes created.
    # Iterate the newly created list and use the original nodes random pointers,
    # to assign references to random pointers for cloned nodes.
    while ptr:
        ptr.next.random = ptr.random.next if ptr.random else None 
        ptr = ptr.next.next

    # Unweave the linked list to get back the original linked list and the cloned list.
    # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
    ptr_old_list = head # A
    ptr_new_list = head.next # A'
    head_new = head.next
    while ptr_old_list:
        ptr_old_list.next = ptr_old_list.next.next # A->B
        ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None # A'->B'
        ptr_old_list = ptr_old_list.next # travers old and new list
        ptr_new_list = ptr_new_list.next
    return head_new

if __name__=='__main__':

    # time: O(n)
    # space: O(1)

    a=Node(7)
    b=Node(13)
    c=Node(11)
    d=Node(10)
    e=Node(1)
    a.next=b
    b.next=c
    b.random=a
    c.next=d
    c.random=e
    d.next=e
    d.random=c
    e.random=a

    f = copyRandomList(a)
    print(a.val==f.val)
    print(f.next.val)
    print(f.random)
    print(f.next.next.val)
    print(f.next.next.random.val)


