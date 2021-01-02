def longestPalSubstr(str):
     
    # Get length of input String
    n = len(str)
     
    # All subStrings of length 1
    # are palindromes
    maxLength = 1
    start = 0
     
    # Nested loop to mark start
    # and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1
             
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
                 
    print("Longest palindrome subString is: ", end = "")
    print(str[start:start + maxLength])
 
    # Return length of LPS
    return maxLength

if __name__ == '__main__':
    
    # time: O(n^2)
    
    print(longestPalSubstr('cabcbaabac'))