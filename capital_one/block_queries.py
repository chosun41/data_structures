class BIT:
    def __init__(self, n):
        self.n = n
        self.l = [0] * (n + 1)
    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.l[i] = max(x, self.l[i])
            i += i & -i
    def query(self, i):
        i += 1
        ans = 0
        while i:
            ans = max(ans, self.l[i])
            i -= i & -i
        return ans

from sortedcontainers import SortedList

def pairwise(iterable):
    # pairwise('ABCDEFG') → AB BC CD DE EF FG
    iterator = iter(iterable)
    a = next(iterator, None)
    for b in iterator:
        yield a, b
        a = b

def getResults(queries):
    sl = SortedList()
    n = min(5 * 10 ** 4, len(queries) * 3)
    sl.add(0)
    sl.add(n)
    
    ans = []
    for q in queries:
        if q[0] == 1:
            x = q[1]
            sl.add(x)
    
    bit = BIT(n + 1)
    for x, y in pairwise(sl):
        bit.add(y, y - x)
    
    for q in reversed(queries):
        if q[0] == 1:
            x = q[1]
            index = sl.index(x)
            after = sl[index + 1]
            before = sl[index - 1]
            sl.remove(x)
            bit.add(after, after - before)
        else:
            _, x, sz = q
            index = sl.bisect_right(x)
            before = sl[index - 1]
            ans.append(bit.query(before) >= sz or (x - before) >= sz)
        
    ans.reverse()
    return ans
    
if __name__ == '__main__':
    print(getResults( queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]))    

    # There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

    # You are given a 2D array queries, which contains two types of queries:

    # For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
    # For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
    # Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

    

    # Example 1:

    # Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

    # Output: [false,true,true]

    # Explanation:



    # For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

    # Example 2:

    # Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

    # Output: [true,true,false]

    # Explanation:



    # Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
    # Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.