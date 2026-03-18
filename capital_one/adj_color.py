def colorTheArray(n, queries):
    nums, c = [0] * n, 0
    ans = [0] * len(queries)
    for i, (index, color) in enumerate(queries):
        pre, nex = nums[index-1] if index > 0 else 0, nums[index+1] if index < n-1 else 0
        if nums[index]: c -= (nums[index] == pre) + (nums[index] == nex)
        nums[index] = color
        c += (nums[index] == pre) + (nums[index] == nex)
        ans[i] = c
    return ans

if __name__ == '__main__':

    print(colorTheArray(n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]))

    # You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

    # Set colors[indexi] to colori.
    # Count the number of adjacent pairs in colors which have the same color (regardless of colori).
    # Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

    

    # Example 1:

    # Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

    # Output: [0,1,1,0,2]

    # Explanation:

    # Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
    # After the 1st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
    # After the 2nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
    # After the 3rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
    # After the 4th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
    # After the 5th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.
    # Example 2:

    # Input: n = 1, queries = [[0,100000]]

    # Output: [0]

    # Explanation:

    # After the 1st query colors = [100000]. The count of adjacent pairs with the same color is 0.

    