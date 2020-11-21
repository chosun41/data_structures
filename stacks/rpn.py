from stack import Stack

def evaluate_rpn(expression: str) -> int:

    rpn_stack=Stack()
    
    # delimiter to separate digits
    delimiter = ','
    
    # dictionary of lambda operators
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y
    }

    # after split by delimiter
    # if token in dictionary
    # push to the stack the lambda function of last two pops
    # otherwise push the number
    # take a peek at the end
    for token in expression.split(delimiter):
        if token in operators:
            rpn_stack.push(operators[token](rpn_stack.pop(), rpn_stack.pop()))
        else:  # token is a number.
            rpn_stack.push(int(token))
    return rpn_stack.peek()


if __name__ == "__main__":
    
    print(evaluate_rpn('1,2,+,3,4,-,+'))
    print(evaluate_rpn('3,4,+,2,*,1,+'))
