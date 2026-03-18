def removeBoxes(boxes):
    n = len(boxes)
    memo = {}

    def dp(l, r, k):
        if l > r:
            return 0

        while l + 1 <= r and boxes[l] == boxes[l + 1]:
            l += 1
            k += 1

        if (l, r, k) in memo:
            return memo[(l, r, k)]

        res = (k + 1) ** 2 + dp(l + 1, r, 0)

        for m in range(l + 1, r + 1):
            if boxes[m] == boxes[l]:
                res = max(res, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))

        memo[(l, r, k)] = res
        return res

    return dp(0, n - 1, 0)


if __name__ == '__main__':

    print(removeBoxes([1,3,2,2,2,3,4,3,1]))


    # You are given several boxes with different colors represented by different positive numbers.

    # You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

    # Return the maximum points you can get.


    # Example 1:

    # Input: boxes = [1,3,2,2,2,3,4,3,1]
    # Output: 23
    # Explanation:
    # [1, 3, 2, 2, 2, 3, 4, 3, 1] 
    # ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
    # ----> [1, 3, 3, 3, 1] (1*1=1 points) 
    # ----> [1, 1] (3*3=9 points) 
    # ----> [] (2*2=4 points)
    # Example 2:

    # Input: boxes = [1,1,1]
    # Output: 9
    # Example 3:

    # Input: boxes = [1]
    # Output: 1