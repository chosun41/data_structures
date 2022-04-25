import heapq

def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type K: int
    :rtype: List[List[int]]
    """
    heapq.heapify(points)
    return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)

if __name__=='__main__':
    # time: O(nlogk)
    # space: O(1)
    print(kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))