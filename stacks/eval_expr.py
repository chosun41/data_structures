def calculate(s):
    num, op, stack = 0, '+', [0] # first op doesn't pop from stack
    ops = {'+':lambda x, y: y, 
           '-':lambda x, y: -y, 
           '*':lambda x, y: x*y, 
           '/':lambda x, y: x//y}
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if not c.isdigit() and c != ' ' or i == len(s)-1:
            prev = 0 if op in '+-' else stack.pop()
            stack.append(ops[op](prev, num))
            num, op = 0, c # reset
    return sum(stack)

if __name__ == '__main__':
    
    # time and space: O(n)
    print(calculate("3+2*2"))
    print(calculate(" 3+5 / 2 "))