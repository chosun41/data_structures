import collections

def numPairsDivisibleBy60(time):
    
    ## dictionary
    # key: remainder of modulo 60
    # value: occurrence of remainder
    residual = collections.defaultdict(int)
    
    ## counter of valid pairs
    counter = 0
    
    ## update the dictionay of remainder
    for t in time:
        
        # remainder of t modulo 60
        remainder = t % 60
        
        # remainder of (60 - t) modulo 60
        complement_remainder = (60 - t) % 60
        
        # find valid pairs with current t, add corresponding pair count
        counter += residual[ complement_remainder ]
        
        # update residual dictionary
        residual[ remainder ] += 1
    
    return counter

if __name__ == '__main__':
    
    #  You are given a list of songs where the ith song has a duration of time[i] seconds.

    # Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

    

    # Example 1:

    # Input: time = [30,20,150,100,40]
    # Output: 3
    # Explanation: Three pairs have a total duration divisible by 60:
    # (time[0] = 30, time[2] = 150): total duration 180
    # (time[1] = 20, time[3] = 100): total duration 120
    # (time[1] = 20, time[4] = 40): total duration 60
    # Example 2:

    # Input: time = [60,60,60]
    # Output: 3
    # Explanation: All three pairs have a total duration of 120, which is divisible by 60.

    print(numPairsDivisibleBy60(time = [30,20,150,100,40]))
    print(numPairsDivisibleBy60(time = [60,60,60]))