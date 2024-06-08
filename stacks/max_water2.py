def trap(bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right] # start out max at ends
    while left < right: 
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max: # important
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    print(trap(bars = [0,1,0,2,1,0,1,3,2,1,2,1])) 
    
    # keep track of left and right max to deduce how much water trapped
    
    # left,right,l_max,r_max,volume = 0,11,0,1,0
    # left,right,l_max,r_max,volume = 1,11,0,1,0

    # left,right,l_max,r_max,volume = 1,11,0,1,0
    # left,right,l_max,r_max,volume = 2,11,1,1,0

    # left,right,l_max,r_max,volume = 2,11,1,1,0
    # left,right,l_max,r_max,volume = 2,11,1,1,1
    # left,right,l_max,r_max,volume = 3,11,1,1,1

    # left,right,l_max,r_max,volume = 3,11,1,1,1
    # left,right,l_max,r_max,volume = 3,11,2,1,1
    # left,right,l_max,r_max,volume = 3,10,2,1,1

    # left,right,l_max,r_max,volume = 3,10,2,1,1
    # left,right,l_max,r_max,volume = 3,10,2,2,1
    # left,right,l_max,r_max,volume = 4,10,2,2,1

    # left,right,l_max,r_max,volume = 4,10,2,2,1
    # left,right,l_max,r_max,volume = 4,10,2,2,2
    # left,right,l_max,r_max,volume = 5,10,2,2,2

    # left,right,l_max,r_max,volume = 5,10,2,2,2
    # left,right,l_max,r_max,volume = 5,10,2,2,4
    # left,right,l_max,r_max,volume = 6,10,2,2,4

    # left,right,l_max,r_max,volume = 6,10,2,2,4
    # left,right,l_max,r_max,volume = 6,10,2,2,5
    # left,right,l_max,r_max,volume = 7,10,2,2,5

    # left,right,l_max,r_max,volume = 7,10,2,2,5
    # left,right,l_max,r_max,volume = 7,10,3,2,5
    # left,right,l_max,r_max,volume = 7,9,3,2,5

    # left,right,l_max,r_max,volume = 7,9,3,2,5
    # left,right,l_max,r_max,volume = 7,9,3,2,6
    # left,right,l_max,r_max,volume = 7,8,3,2,6

    # left,right,l_max,r_max,volume = 7,8,3,2,6
    # left,right,l_max,r_max,volume = 7,7,3,2,6