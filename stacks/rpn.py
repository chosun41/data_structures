# reverse polish notation evaluate to integer
def evaluate_rpn(expression: str) -> int:

    stack=[]

    ops = {'+':lambda y,x:x+y,
            '-':lambda y,x:x-y,
            '*':lambda y,x:x*y,
            '/':lambda y,x: x//y} #y,x not x,y

    for x in expression.split(","):
        if x in ops:
            stack.append(ops[x](stack.pop(),stack.pop()))
        else:
            stack.append(int(x))

    return stack[0]

if __name__ == "__main__":
    
    print(evaluate_rpn('1,2,+,3,4,-,+'))
    print(evaluate_rpn('3,4,+,2,*,1,+'))