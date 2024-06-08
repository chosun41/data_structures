from collections import deque

class Solution(object):
    
    def calculate(self, s):
         
        arr = deque()
        for x in s+'+':
            arr.append(x)
        return self.helper(arr)

    def helper(self, s):
        if len(s) == 0:
            return 0
        stack=[]
        preop='+'
        num=0
        while s:
            c = s.popleft()
            if c.isdigit():
                num = num*10 + int(c)
            if c=='(':
                num = self.helper(s) # num = self.helper
            if c in '+-*/)':
                if preop=='+':
                    stack.append(num)
                elif preop=='-':
                    stack.append(-num)
                elif preop=='*':
                    operant = stack.pop()
                    stack.append(operant*num)
                elif preop=='/':
                    operant = stack.pop()
                    stack.append(operant//num)
                preop = c
                num = 0
                if preop==')': # this has to be at the end
                    break
        return sum(stack)


if __name__=='__main__':

    # time and space O(n) because of recursion

    x = Solution()
    print(x.calculate("1 + 1"))
    print(x.calculate(" 6-4 / 2 " ))
    print(x.calculate("2*(5+5*2)/3+(6/2+8)" ))
    print(x.calculate("(2+6* 3+5- (3*14/7+2)*5)+3" )) 
    print(x.calculate("(1+(4+5+2)-3)+(6+8)"))