
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, root):
        first = second = 0  # base case for leaf, first store the maximum depth, second is second maximum depth
        for neighbor in root.children:
            depth = self.dfs(neighbor)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth
        self.diameter = max(self.diameter, first + second)
        return first + 1

if __name__=='__main__':

    # find diameter of nary tree
    # time and space: O(n)

    x = Node(5)
    y = Node(6)
    z = Node(3,[x,y])
    b = Node(2)
    c = Node(4)
    a = Node(1,[z,b,c])

    d = Solution()
    print(d.diameter(a))

    a = Node(5)
    b = Node(6)
    c = Node(3,[a])
    d = Node(4,[b])
    e = Node(2,[c,d])
    f = Node(1,[e])

    g = Solution()
    print(g.diameter(f))