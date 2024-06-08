class MinStack:
    
    def __init__(self):
        self.stk = []
        self.minStk = []        

    def push(self, val: int) -> None:
        if not self.minStk or val <= self.minStk[-1]: 
            self.minStk.append(val)
        self.stk.append(val)            

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1]:
            self.minStk.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]

if __name__=='__main__':

    #     Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    # Implement the MinStack class:

    # MinStack() initializes the stack object.
    # void push(int val) pushes the element val onto the stack.
    # void pop() removes the element on the top of the stack.
    # int top() gets the top element of the stack.
    # int getMin() retrieves the minimum element in the stack.
    

    # Example 1:

    # Input
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]

    # Output
    # [null,null,null,null,-3,null,0,-2]

    # Explanation
    # MinStack minStack = new MinStack();
    # minStack.push(-2);
    # minStack.push(0);
    # minStack.push(-3);
    # minStack.getMin(); // return -3
    # minStack.pop();
    # minStack.top();    // return 0
    # minStack.getMin(); // return -2

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3) # stk = [-2,0,-3] minStk = [-2,-3]
    print(minStack.getMin()) # // return -3
    minStack.pop()
    print(minStack.top()) #   // return 0
    print(minStack.getMin()) # // return -2