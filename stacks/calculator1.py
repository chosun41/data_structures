def calculate(s: str) -> int:
        num = 0
        pre_op = '+'
        s+='+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == ' ':
                    pass
            else:
                if pre_op == '+': #pre op not c
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant*num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(int(operant/num))
                num = 0
                pre_op = c
        return sum(stack)

if __name__=='__main__':
    print(calculate(" 3+5 / 2 "))

    # c = "3"
    # num, pre_op, stack = 0, +, []
    # num, pre_op, stack = 3, +, []

    # c = "+"
    # num, pre_op, stack = 3, +, []
    # num, pre_op, stack = 0, +, [3]

    # c = "5"
    # num, pre_op, stack = 0, +, [3]
    # num, pre_op, stack = 5, +, [3]

    # c = "/"
    # num, pre_op, stack = 5, +, [3]
    # num, pre_op, stack = 0, /, [3,5]

    # c = "2"
    # num, pre_op, stack = 0, /, [3,5]
    # num, pre_op, stack = 2, /, [3,5]

    # c = "+"
    # num, pre_op, stack = 2, /, [3,5]
    # num, pre_op, stack = 0, +, [3, 2]
    # sum = 5

    print(calculate("3+2*2"))