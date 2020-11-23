from stack import Stack
import re

def infixToPostfix(infixexpr):
    
    # priority of operations
    prec = {"*":3,
           "/":3,
           "+":2,
           "-":2,
           "(":1}
    
    opStack = Stack()
    
    # empty post fix list
    postfixList = []
    
    # split by spaces
    tokenList = infixexpr.split()

    # if alphanumeric, then append to postfixlist
    # if left parentheses, push to opstack
    # if right parentheses, pop from opstack and while popped element is not left parenthesis append to postfixlist
    
    # if not alphanumeric, then while opstack is not empty and the opstack peek priority is greater than the current token operator priority
    # then append to postfixlist from opstack popped
    # push the final token to opstack
    
    # empty out the rest of opstack
    # return new string from postfixlist
    for token in tokenList:
        if re.match('^[a-zA-Z0-9_]+$',token):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]:
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return " ".join(postfixList)

if __name__ == "__main__":
    
    print(infixToPostfix("A * B + C * D"))
    # 0.opStack = []
    #   postfixList = [A]
    # 1.opStack = [*]
    #   postfixList = [A]
    # 2.opStack = [*]
    #   postfixList = [A B]
    # 3.opStack = [+]
    #   postfixList = [A B *] - * > +
    # 4.opStack = [+]
    #   postfixList = [A B * C]
    # 5.opStack = [+ *]
    #   postfixList = [A B * C] - + < *
    # 6.opStack = [+ *]
    #   postfixList = [A B * C D] 
    #   opStack = []
    #   postfixList = [A B * C D * +] 
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # 0.opStack = [(]
    #   postfixList = []
    # 1.opStack = [(]
    #   postfixList = [A]
    # 2.opStack = [( +]
    #   postfixList = [A] - ( < +
    # 3.opStack = [( +]
    #   postfixList = [A B] 
    # 4.opStack = []
    #   postfixList = [A B +] - ) start popping from opstack
    # 5.opStack = [*]
    #   postfixList = [A B +] 
    # 6.opStack = [*]
    #   postfixList = [A B + C] 
    # 7.opStack = [-]
    #   postfixList = [A B + C *] - * > -
    # 8.opStack = [- (]
    #   postfixList = [A B + C *] 
    # 9.opStack = [- (]
    #   postfixList = [A B + C * D] 
    # 10.opStack = [- ( -]
    #    postfixList = [A B + C * D] - ( < -
    # 11.opStack = [- ( -]
    #    postfixList = [A B + C * D E] 
    # 12.opStack = [-]
    #    postfixList = [A B + C * D E -] - ) start popping from opstack
    # 13.opStack = [- *]
    #    postfixList = [A B + C * D E -] 
    # 14.opStack = [- * (]
    #    postfixList = [A B + C * D E -] 
    # 15.opStack = [- * ( ]
    #    postfixList = [A B + C * D E - F] 
    # 16.opStack = [- * ( +]
    #    postfixList = [A B + C * D E - F ] 
    # 17.opStack = [- * ( +]
    #    postfixList = [A B + C * D E - F G] 
    # 18.opStack = [- * ]
    #    postfixList = [A B + C * D E - F G +] - ) start popping from opstack
    #    opStack = []
    #    postfixList = [A B + C * D E - F G + * -] 