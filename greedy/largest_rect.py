def calculate_largest_rectangle(heights):

    pillar_indices = []
    max_rectangle_area = 0
    # By appending [0] to heights, we can uniformly handle the computation for
    # rectangle area here.
    for i, h in enumerate(heights + [0]):
        while pillar_indices and heights[pillar_indices[-1]] >= h:
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)
    return max_rectangle_area

if __name__ == '__main__':
    
    # O(n)
    # heights of building, find max area of recntagle under the skyline
    # all the buildings have to be 
    print(calculate_largest_rectangle([0,4,2,5,6,3,2,6,6,5,2,1,3]))
