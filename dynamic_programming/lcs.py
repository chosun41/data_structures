def longestCommonSubsequence(text1, text2):
    # Get the lengths of both input strings
    len_text1, len_text2 = len(text1), len(text2)
    
    # Initialize a 2D array (list of lists) with zeros for dynamic programming
    # The array has (len_text1 + 1) rows and (len_text2 + 1) columns
    dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
    
    # Loop through each character index of text1 and text2
    for i in range(1, len_text1 + 1):
        for j in range(1, len_text2 + 1):
            # If the characters match, take the diagonal value and add 1
            if text1[i - 1] == text2[j - 1]:
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
            else:
                # If the characters do not match, take the maximum of the value from the left and above
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
    
    # The bottom-right value in the matrix contains the length of the longest common subsequence
    return dp_matrix[len_text1][len_text2]

if __name__=='__main__':
    
    # least common subsequence, left to right not necessarily contiguous sequence
    # lcslength2 - time: O(mn), space: O(mn) (b/c of table)
    print("Longest common subsequence: ", longestCommonSubsequence('ABCBDAB', 'BDCABA'))
    
    #        0  1  2  3  4  5  6
    #           B  D  C  A  B  A
    #  0   [[0, 0, 0, 0, 0, 0, 0], 
    #  1 A  [0, 0, 0, 0, 1, 1, 1], 
    #  2 B  [0, 1, 1, 1, 1, 2, 2], 
    #  3 C  [0, 1, 1, 2, 2, 2, 2], 
    #  4 B  [0, 1, 1, 2, 2, 3, 3], 
    #  5 D  [0, 1, 2, 2, 2, 3, 3], 
    #  6 A  [0, 1, 2, 2, 3, 3, 4], 
    #  7 B  [0, 1, 2, 2, 3, 4, 4]]
    # x=7,y=6, T[7][6]=T[6][6], x=6,y=6
    # x=6,y=6  T[6][6]!=T[5][6],T[6][6]!=T[6][5],result='A'
    # x=5,y=5  T[5][5]=T[4][5],x=4,y=5
    # x=4,y=5  T[4][5]!=T[3][5],T[4][5]!=T[4][4],result='BA'
    # x=3,y=4  T[3][4]!=T[2][4],T[3][4]=T[3][3],x=3,y=3
    # x=3,y=3  T[3][3]!=T[2][3],T[3][3]!=T[3][2],result='CBA'
    # x=2,y=2  T[2][2]!=T[1][2],T[2][2]=T[2][1],x=2,y=1
    # x=2,y=1  T[2][1]!=T[1][1],T[2][1],T[2][0],result='BCBA'
    # x=1,y=0 stop