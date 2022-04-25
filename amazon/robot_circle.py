
def isRobotBounded(instructions):
    direction = 0
    x, y = 0, 0
    for c in instructions:
        if c == 'G':
            if direction == 0: # up
                y += 1
            elif direction == 1: # left
                x -= 1
            elif direction == 2: # down
                y -= 1
            else: # right
                x += 1
        elif c == 'L':
            direction += 1
        elif c == 'R':
            direction -= 1
        
        # reset direction if 360 degrees
        # alternative 1-liner: direction %= 4
        if direction == 4:
            direction = 0
    
    return (x == 0 and y == 0) or direction != 0

if __name__ == '__main__':
    
    # On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

    # "G": go straight 1 unit;
    # "L": turn 90 degrees to the left;
    # "R": turn 90 degrees to the right.
    # The robot performs the instructions given in order, and repeats them forever.

    # Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

    

    # Example 1:

    # Input: instructions = "GGLLGG"
    # Output: true
    # Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
    # When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
    # Example 2:

    # Input: instructions = "GG"
    # Output: false
    # Explanation: The robot moves north indefinitely.
    # Example 3:

    # Input: instructions = "GL"
    # Output: true
    # Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

    print(isRobotBounded(instructions = "GL"))
    print(isRobotBounded(instructions = "GGLLGG"))