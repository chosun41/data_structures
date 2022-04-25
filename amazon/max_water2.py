def trap(bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right: 
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max: # important
            volume += l_max - bars[left] # all l
            left += 1
        else:
            volume += r_max - bars[right] # all r
            right -= 1
    return volume

if __name__=='__main__':
    # time: O(n)
    # space: O(1)
    print(trap(bars = [0,1,0,2,1,0,1,3,2,1,2,1]))
    
    # i=0,j=11,l=0,r=1,i=1,l=1,res=0
    # i=1,j=11,l=1,r=1,i=2,res=1
    # i=2,j=11,i=3,l=2,res=1
    # i=3,j=11,j=10,r=2,res=1
    # i=3,j=10,i=4,res=2
    # i=4,j=10,i=5,res=4
    # i=5,j=10,i=6,res=5
    # i=6,j=10,i=7,l=3
    # i=7,j=10,j=9,res=6
    # i=7,j=9,j=8,r=2
    # i=7,j=8,j=7,r=3