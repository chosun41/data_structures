import collections
from collections import deque

def findCircleNum(isConnected):
    dic = collections.defaultdict(list)

    for idx, clist in enumerate(isConnected):
        for i,c in enumerate(clist):
            if c ==1:
                dic[idx+1].append(i+1)

    print(dic)

    res = 0
    seen = set()
    queue = deque()
    for d in dic:
        if d not in seen:
            queue.append(d)
            seen.add(d)
            print(d,queue,seen)
            while queue:
                val = queue.popleft()
                for x in dic[val]:
                    if x not in seen:
                        queue.append(x)
                        seen.add(x)
            print(queue,seen)
            print()

            res+=1
        
    return res

if __name__ == '__main__':
    
    #  There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

    # A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    # You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    # Return the total number of provinces.

    

    # Example 1:


    # Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    # Output: 2
    # Example 2:


    # Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    # Output: 3
    

    # Constraints:

    # 1 <= n <= 200
    # n == isConnected.length
    # n == isConnected[i].length
    # isConnected[i][j] is 1 or 0.
    # isConnected[i][i] == 1
    # isConnected[i][j] == isConnected[j][i]

    print(findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
    print(findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))

  