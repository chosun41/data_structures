def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    prev_count = 0
    cur_count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += min(prev_count, cur_count)
            prev_count = cur_count #
            cur_count = 1 # reset current
        else:
            cur_count += 1
        print(i,res,prev_count,cur_count)
    res += min(prev_count, cur_count)
    return res

if __name__ == '__main__':
    
    # give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

    # Substrings that occur multiple times are counted the number of times they occur.

    

    # Example 1:

    # Input: s = "00110011"
    # Output: 6
    # Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    # Notice that some of these substrings repeat and are counted the number of times they occur.
    # Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
    # Example 2:

    # Input: s = "10101"
    # Output: 4
    # Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

    print(countBinarySubstrings(s = "00110011")) 
    # i=1,cur_count=2
    # i=2,res=0,prev_count=2,cur_count=1
    # i=3,cur_count=2
    # i=4,res=2 01,0011,cur_count=1
    # i=5,cur_count=2
    # i=6,res=4,01,0011,0110,10,cur_count=1
    # i=7,cur_count=2
    # res = 01,0011,0110,10,01,10001
    print(countBinarySubstrings(s = "10101"))
    print(countBinarySubstrings(s = '00011111')) #000 1111

    # prev_count - keeps track of prev_countious continuous count
    # cur_count - keeps track of current continuous count
    # res - whenever there is no match between s[i] and s[i-1] update res and set prev_count to cur_count and cur_count to 1
    # also at end update res

    # binary substring of equal 0s and 1s is decided by the minimal continuous occurrence between character groups

    # Example:

    # Given s = 00011111

    # 0's continuous occurrence = 3
    # 1's continuous occurrence = 5

    # min(3, 5) = 3

    # There are 3 binary substrings of equal 0s and 1s as following:

    # 01
    # 0011
    # 000111