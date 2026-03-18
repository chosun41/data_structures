def fullBloomFlowers(flowers, people):
    n = len(flowers)
    start = [flowers[i][0] for i in range(n)]
    end = [flowers[i][1] + 1 for i in range(n)]
    start.sort()
    end.sort()
    ans = [0] * len(people)
    for i in range(len(people)):
        e = binarySearch(end, people[i])
        s = binarySearch(start, people[i])
        ans[i] = s - e
    return ans

def binarySearch(A, target):
    l, r = 0, len(A)
    while l < r:
        mid = (l + r) // 2
        if target < A[mid]:
            r = mid
        else:
            l = mid + 1
    return l

if __name__ == '__main__':

    # You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

    # Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

    print(fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]))
    print(fullBloomFlowers([[1,10],[3,3]], people = [3,3,2]))

    # Example 1:


    # Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
    # Output: [1,2,2,2]
    # Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
    # For each person, we return the number of flowers in full bloom during their arrival.
    # Example 2:


    # Input: flowers = [[1,10],[3,3]], people = [3,3,2]
    # Output: [2,2,1]
    # Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
    # For each person, we return the number of flowers in full bloom during their arrival.
