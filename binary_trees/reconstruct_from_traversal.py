class TreeNode:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

def buildTree(preorder, inorder):
    
    # both have to be lists that are populated and same size
    if inorder: 
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root
    
if __name__ == '__main__':
    
    root=buildTree([1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15],[8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15])
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    print(root.left.left.val)
    print(root.right.right.val)
    
    # preorder - [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15]
    # inorder - [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]

    #          1 
    #     2          3    
    #  4    5      6    7
    # 8 9  10 11 12 13 14 15 
    #    root - 1
    #    rootPos - 7
    #    root.left = buildTree(preorder[1:8],inorder[:7]) -> buildTree([2, 4, 8, 9, 5, 10, 11],[8, 4, 9, 2, 10, 5, 11])
    #    root.right = buildTree(preorder[8:],inorder[8:]) -> buildTree( [3, 6, 12, 13, 7, 14, 15],[12, 6, 13, 3, 14, 7, 15])
    
    # root.left root - 2
    #            rootPos - 3
    #            root.left = buildTree(preorder[1:4],inorder[:3]) -> buildTree([4,8,9],[8,4,9])
    #            root.right = buildTree(preorder[4:],inorder[4:]) -> buildTree([5,10,11],[10,5,11])
    
    # root.left.left  root - 4
    #                 rootPos - 1
    #                 root.left = buildTree(preorder[1:2],inorder[:1]) -> buildTree([8],[8])
    #                 root.right = buildTree(preorder[2:],inorder[2:]) -> buildTree([9],[9])
    
    # root.left.right  root - 5
    #                  rootPos - 1
    #                  root.left = buildTree(preorder[1:2],inorder[:1]) -> buildTree([10],[10])
    #                  root.right = buildTree(preorder[2:],inorder[2:]) -> buildTree( [11],[11])
    
    # root.left.left.left  root - 8
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])
    
    # root.left.left.right  root - 9
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])

    # root.left.right.left  root - 10
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])

    # root.left.right.left  root - 11
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])
    
    # root.right root - 3
    #            rootPos - 3
    #            root.left = buildTree(preorder[1:4],inorder[:3]) -> buildTree([6, 12, 13],[12, 6, 13])
    #            root.right = buildTree(preorder[4:],inorder[4:]) -> buildTree([7, 14, 15],[14, 7, 15])
    
    # root.right.left  root - 6
    #                 rootPos - 1
    #                 root.left = buildTree(preorder[1:2],inorder[:1]) -> buildTree([12],[12])
    #                 root.right = buildTree(preorder[2:],inorder[2:]) -> buildTree([13],[13])
    
    # root.right.right  root - 7
    #                  rootPos - 1
    #                  root.left = buildTree(preorder[1:2],inorder[:1]) -> buildTree([14],[14])
    #                  root.right = buildTree(preorder[2:],inorder[2:]) -> buildTree( [15],[15])
    
    # root.right.left.left  root - 12
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])
    
    # root.right.left.right  root - 13
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])

    # root.right.right.left  root - 14
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])

    # root.right.right.left  root - 15
    #                      rootPos - 0
    #                      root.left = buildTree(preorder[1:1],inorder[:0]) -> buildTree([],[])
    #                      root.right = buildTree(preorder[1:],inorder[1:]) -> buildTree([],[])