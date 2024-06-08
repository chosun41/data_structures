
class Node:

    def __init__(self,val=None,next=None,random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    dic={None:None}
    cur=head
    while cur: # store the node in the dictionary
        dic[cur]=Node(cur.val)
        cur=cur.next
    cur=head
    while cur:
        copy=dic[cur]
        copy.next=dic[cur.next]
        copy.random=dic[cur.random]
        cur=cur.next
    return dic[head]

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


