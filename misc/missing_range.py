def findMissingRanges(nums,lower,upper):
    # formats range in the requested format
    def formatRange(lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)

    result = []
    prev = lower - 1
    for i in range(len(nums) + 1):
        curr = nums[i] if i < len(nums) else upper + 1
        if prev + 1 <= curr - 1:
            result.append(formatRange(prev + 1, curr - 1))
        prev = curr
    return result

if __name__ == '__main__':

    # You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

    # A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

    # Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
    
    # time: O(n)
    # space: O(1)
    print(findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))