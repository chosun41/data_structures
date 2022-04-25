# pivot everything less than pivot to start, equal to pivot to middle, and larger than middle to the end
# time: O(n) space:O(1)

def sortColors(nums):
    """
    Dutch National Flag problem solution.
    """
    # for all idx < p0 : nums[idx < p0] = 0
    # curr is an index of element under consideration
    p0 = curr = 0
    # for all idx > p2 : nums[idx > p2] = 2
    p2 = len(nums) - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
    return nums

    
if __name__ == '__main__':
    print(sortColors([0,1,2,0,2,1,1]))
    # p0=0,curr=0,p2=6,[0,1,2,0,2,1,1],p0=1,curr=1,p2=6
    # p0=1,curr=1,p2=6,[0,1,2,0,2,1,1],p0=1,curr=2,p2=6
    # p0=1,curr=2,p2=6,[0,1,1,0,2,1,2],p0=1,curr=2,p2=5
    # p0=1,curr=2,p2=5,[0,1,1,0,2,1,2],p0=1,curr=3,p2=5
    # p0=1,curr=3,p2=5,[0,0,1,1,2,1,2],p0=2,curr=4,p2=5
    # p0=2,curr=4,p2=5,[0,0,1,1,1,2,2],p0=2,curr=4,p2=4
    # p0=2,curr=4,p2=4,[0,0,1,1,1,2,2],p0=2,curr=5,p2=4
    print(sortColors([2,1,0]))