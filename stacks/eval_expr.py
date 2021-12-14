def calculate(s):
    s+='+'
    num, preop, stack = 0, '+', [] # first op doesn't pop from stack
    ops = {'+':lambda x, y: y, 
           '-':lambda x, y: -y, 
           '*':lambda x, y: x*y, 
           '/':lambda x, y: x//y}
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        elif c==' ':
            continue
        else:
            prev = 0 if preop in '+-' else stack.pop() # op not c
            stack.append(ops[preop](prev, num))
            num, preop = 0, c # reset
    return sum(stack) # important

if __name__ == '__main__':
    
    # time and space: O(n)
    print(calculate("3+2*2"))
    # num=0,op=+,stack=[0]
    # i=0,c=3,num=3
    # i=1,c=+,prev=0,stack=[0,3],num=0,op=+
    # i=2,c=2,num=2
    # i=3,c=*,prev=0,stack=[0,3,2],num=0,op=*
    # i=4,c=2,num=2,prev=2,stack=[0,3,4],num=0,op=2
    print(calculate("3+5/2"))
    # num=0,op=+,stack=[0]
    # i=0,c=3,num=3
    # i=1,c=+,prev=0,stack=[0,3],num=0,op=+
    # i=2,c=5,num=5
    # i=3,c=/,prev=0,stack=[0,3,5],num=0,op=/
    # i=4,c=2,prev=5,stack=[0,3,2],num=0,op=2