class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def evaluateExpressionTree(root): 
  
    # empty tree 
    if not root: 
        return 0
  
    # leaf node 
    if not root.left and not root.right: 
        return int(root.val)
  
    # evaluate left tree 
    left_sum = evaluateExpressionTree(root.left) 
  
    # evaluate right tree 
    right_sum = evaluateExpressionTree(root.right) 
  
    # check which operation to apply 
    if root.val == '+': 
        return left_sum + right_sum 
      
    elif root.val == '-': 
        return left_sum - right_sum 
      
    elif root.val == '*': 
        return left_sum * right_sum 
      
    elif root.val == '/': 
        return left_sum / right_sum 
  
if __name__=='__main__': 
      
    # creating a sample tree 
    root = TreeNode('+') 
    root.left = TreeNode('*') 
    root.left.left = TreeNode('5') 
    root.left.right = TreeNode('4') 
    root.right = TreeNode('-') 
    root.right.left = TreeNode('100') 
    root.right.right = TreeNode('20') 
    print(evaluateExpressionTree(root))

    #creating a sample tree 
    root = TreeNode('+') 
    root.left = TreeNode('*') 
    root.left.left = TreeNode('5') 
    root.left.right = TreeNode('4') 
    root.right = TreeNode('-') 
    root.right.left = TreeNode('100') 
    root.right.right = TreeNode('/') 
    root.right.right.left = TreeNode('20') 
    root.right.right.right = TreeNode('2') 
    print(evaluateExpressionTree(root))