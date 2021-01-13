
def addOperators(num, target):
    def backtracking(i, path, resultSoFar, prev):
        if i == len(num):
            if resultSoFar == target:
                ans.append(path)
            return

        for j in range(i, len(num)):
            if j > i and num[i] == '0': 
                continue  # Skip leading zero number
            now = int(num[i:j + 1])
            if i == 0:
                backtracking(j + 1, path + str(now), resultSoFar + now, now)  # First num, pick it without adding any operator
            else:
                backtracking(j + 1, path + "+" + str(now), resultSoFar + now, now)
                backtracking(j + 1, path + "-" + str(now), resultSoFar - now, -now)
                backtracking(j + 1, path + "*" + str(now), resultSoFar - prev + prev * now, prev * now)  # Can imagine with example: 1+2*3*4

    ans = []
    backtracking(0, "", 0, 0)
    return ans

if __name__=='__main__':
    # get to target by adding operators in b/t numbers
    # time: O(n * 4^n) - 4 choices between +,-,x,or no operator
    # space: O(n)
    print(addOperators(num = "105", target = 5))
    # i=0,path='',resultSoFar=0,prev=0
    # j=0,now=1
        # backtrack(1,'1',1,1)
        # i=1,j=1,now=0
            # backtrack(2,'1+0',1,0)
                # i=2,j=2,now=5
                # backtrack(3,'1+0+5',6,5) x
                # backtrack(3,'1+0-5',-4,-5) x
                # backtrack(3,'1+0*5',0,0) x
            # backtrack(2,'1-0',1,0)
                # i=2,j=2,now=5
                # backtrack(3,'1-0+5',6,5) x
                # backtrack(3,'1-0-5',-4,-5) x
                # backtrack(3,'1-0*5',0,0) x
            # backtrack(2,'1*0',0,0)
                # i=2,j=2,now=5
                # backtrack(3,'1*0+5',5,5) ans=['1*0+5']
                # backtrack(3,'1*0-5',-4,-5) x
                # backtrack(3,'1*0*5',0,0) x
        # i=1,j=2
            # continue
    # j=1,now=10
        # backtrack(2,'10',10,10)
        # i=2,j=2,now=5
            # backtrack(3,'10+5',15,5),ans=['1*0+5','10+5']
            # backtrack(3,'10-5',10,-5) x
            # backtrack(3,'10*5',50,50) x
    # j=2,now=105
        # backtrack(3,'105',105,105) x
  