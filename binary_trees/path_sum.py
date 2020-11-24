from binary_tree import BinaryTree

def pathFinder(root, val, path, paths):
    if not root:
        return False
    
    # when you reached the leaves
    if not root.left and not root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False
    
    left = pathFinder(root.left, val - root.data, path + [root.data], paths)
    right = pathFinder(root.right, val - root.data, path + [root.data], paths)  # make sure it can be executed!
    return left or right

def hasPathWithSum(root, val):
    paths = []
    pathFinder(root, val, [], paths)
    print('sum:', val)
    print('paths:', paths)

if __name__ == '__main__':
    
    # find a path from root to leave in binary tree which has indicated sum
    
    root1 = BinaryTree(1)
    root1.insertLeft(2)
    root1.insertRight(3)
    root1.getLeft().insertLeft(4)
    root1.getLeft().insertRight(5)
    root1.getRight().insertLeft(6)
    root1.getRight().insertRight(7)
    
    hasPathWithSum(root1, 4)
    hasPathWithSum(root1, 11)
    hasPathWithSum(root1, 8)