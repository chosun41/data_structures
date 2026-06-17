class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1
        
        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            
            # Save cur_max before it gets updated
            tmp_max = cur_max * n
            tmp_min = n * cur_min
            cur_max = max(tmp_max, tmp_min, n)
            cur_min = min(tmp_max, tmp_min, n)
            res = max(res, cur_max)
            
        return res

# --- Test Example ---
if __name__ == "__main__":

    # Given an integer array nums, find a subarray that has the largest product, and return the product.

    # The test cases are generated so that the answer will fit in a 32-bit integer.

    # Note that the product of an array with a single element is the value of that element.

    

    # Example 1:

    # Input: nums = [2,3,-2,4]
    # Output: 6
    # Explanation: [2,3] has the largest product 6.
    # Example 2:

    # Input: nums = [-2,0,-1]
    # Output: 0
    # Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    

    # Constraints:
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))   # Expected: 6
    print(sol.maxProduct([-2,0,-1]))    # Expected: 0
    print(sol.maxProduct([-2,3,-4]))    # Expected: 24