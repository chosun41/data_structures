def removeDuplicates(s,k):

    char_stack = [ ('bottom', 0) ]

    for char in s:

        if char == char_stack[-1][0]:
            # update last character's length of adjacency
            last_char, last_adj_len = char_stack.pop()
            char_stack.append( (last_char, last_adj_len+1) )

        else:
            # push character with length of adjacency = 1
            char_stack.append( ( char, 1) )

        if char_stack[-1][1] == k:
            # pop last character if it has repeated k times

            char_stack.pop()

    output_str = ""
    for i in range( len(char_stack) ):
        output_str += char_stack[i][0] * char_stack[i][1]

    return output_str

if __name__=='__main__':
    # time and space: O(n)
    # remove substrings of size k if they are duplicates
    print(removeDuplicates(s = "deeedbbcccbdaa", k = 3))
    print(removeDuplicates(s = "pbbcggttciiippooaais", k = 2))
                       