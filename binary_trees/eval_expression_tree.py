from binary_tree import BinaryTree

def evaluateExpressionTree(root): 
  
    # empty tree 
    if root is None: 
        return 0
  
    # leaf node 
    if root.left is None and root.right is None: 
        return int(root.data) 
  
    # evaluate left tree 
    left_sum = evaluateExpressionTree(root.left) 
  
    # evaluate right tree 
    right_sum = evaluateExpressionTree(root.right) 
  
    # check which operation to apply 
    if root.data == '+': 
        return left_sum + right_sum 
      
    elif root.data == '-': 
        return left_sum - right_sum 
      
    elif root.data == '*': 
        return left_sum * right_sum 
      
    else: 
        return left_sum / right_sum 
  
if __name__=='__main__': 
      
    # creating a sample tree 
    root = BinaryTree('+') 
    root.left = BinaryTree('*') 
    root.left.left = BinaryTree('5') 
    root.left.right = BinaryTree('4') 
    root.right = BinaryTree('-') 
    root.right.left = BinaryTree('100') 
    root.right.right = BinaryTree('20') 
    print(evaluateExpressionTree(root))

    #creating a sample tree 
    root = BinaryTree('+') 
    root.left = BinaryTree('*') 
    root.left.left = BinaryTree('5') 
    root.left.right = BinaryTree('4') 
    root.right = BinaryTree('-') 
    root.right.left = BinaryTree('100') 
    root.right.right = BinaryTree('/') 
    root.right.right.left = BinaryTree('20') 
    root.right.right.right = BinaryTree('2') 
    print(evaluateExpressionTree(root))