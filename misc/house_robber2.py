class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def simple_rob(h_list):
            # Option A: Rob current house (n) + the max from two houses ago (rob1)
            # Option B: Skip current house and keep the max from one house ago (rob2)
            rob1, rob2 = 0, 0
            for n in h_list:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        # break into two linear so as to not deal with circular
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

# --- Test Examples ---
if __name__ == "__main__":

    # You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

    # Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

    

    # Example 1:

    # Input: nums = [2,3,2]
    # Output: 3
    # Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
    # Example 2:

    # Input: nums = [1,2,3,1]
    # Output: 4
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.
    # Example 3:

    # Input: nums = [1,2,3]
    # Output: 3
    

    # Constraints:

    # 1 <= nums.length <= 100
    # 0 <= nums[i] <= 1000
    sol = Solution()
    print(sol.rob([2,3,2]))   # Expected: 3
    print(sol.rob([1,2,3,1])) # Expected: 4