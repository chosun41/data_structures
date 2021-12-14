def findBuildings(heights):
    n = len(heights)
    answer = []
    max_height = -1
    
    for current in reversed(range(n)):
        # If there is no building higher (or equal) than the current one to its right,
        # push it in the answer array.
        if max_height < heights[current]:
            answer.append(current)
        
            # Update max building till now.
            max_height = heights[current]
    
    answer.reverse()
    return answer

if __name__ == '__main__':

    # There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

    # The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

    # Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

    # time: O(n)
    # space: O(1)

    print(findBuildings([4,2,3,1]))

    print(findBuildings([1,3,2,4]))