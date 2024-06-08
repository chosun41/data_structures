class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

import collections

def distanceK(root, target, k):
    def dfs(node, par = None): # two arugments
        if node:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    queue = collections.deque([(target, 0)])
    seen = {target}
    while queue:
        if queue[0][1] == k:
            return [node.val for node, d in queue]
        node, d = queue.popleft()
        if node:
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

    return []

if __name__ == '__main__':

    # Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

    # You can return the answer in any order.

    # time and space: O(n)

    x = TreeNode(3)
    x.left = TreeNode(5)
    x.right = TreeNode(1)
    x.left.left = TreeNode(6)
    x.left.right = TreeNode(2)
    x.left.right.left = TreeNode(7)
    x.left.right.right = TreeNode(4)
    x.right.left = TreeNode(0)
    x.right.right = TreeNode(8)

    #       3
    #   5      1
    #  6  2   0  8
    #   7  4

    print(distanceK(x, target = x.left, k = 2))
