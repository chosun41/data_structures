def get_max_trapped_water(heights):

    i, j, max_water = 0, len(heights) - 1, 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        else:  # heights[i] <= heights[j].
            i += 1
    return max_water

if __name__ == '__main__':
    
    # time: O(n)
    # imagine each as height of water, and width between indexes is width,find max area of water b/t two points
    # of min height until i crosses j
    print(get_max_trapped_water([1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1]))
    
    # i=0,j=17,height=1,area=17
    # i=1,j=17,height=1,area=17
    # i=1,j=16,height=2,area=30
    # i=2,j=16,height=1,area=14
    # i=3,j=16,height=3,area=39
    # i=4,j=16,height=4,area=48
    # i=5,j=16,height=4,area=44
    # i=6,j=16,height=4,area=40
    # i=6,j=15,height=2,area=18
    # i=6,j=14,height=1,area=12
    # i=6,j=13,height=2,area=14
    # i=6,j=12,height=3,area=18
    # i=6,j=11,height=1,area=5
    # i=6,j=10,height=3,area=12
    # i=6,j=9,height=1,area=3
    # i=6,j=8,height=2,area=4
    # i=6,j=7,height=5,area=5