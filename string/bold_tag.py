def addBoldTag(s,dict):
    # Initialize a list of booleans for each character in s.
    bold = [False for _ in range(len(s))]
    
    # Iterate through the dictionary, marking words to be bolded as True.
    for word in dict:
        # Mark every occurrence of the word as True.
        start = s.find(word)
        while start != -1:
            for i in range(start, len(word) + start):
                bold[i] = True
            start = s.find(word,start+1) # next index
    
    # Initialize the output list of strings.
    output = []
    
    # Traverse the input string, building the output list.
    i = 0
    while i < len(s):
        # If the current character is to be bolded...
        if bold[i]:
            # Insert a bold tag.
            output.append("<b>")
            # Append characters to be bolded.
            while i < len(s) and bold[i]: # while i<len(s)
                output.append(s[i])
                i += 1
            # Insert the end tag.
            output.append("</b>")
        # Otherwise, just append the character.
        else:
            output.append(s[i])
            i += 1
    
    # Join the output list and return it.
    return "".join(output)

if __name__ =='__main__':
    # time: O(s*l) s-length of string l - length of longest word in word dict
    S = "abcxyz123"
    words = ["abc","123"]
    print(addBoldTag(S,words))
    S = "aaabbcc"
    words = ["aaa","aab","bc"]
    print(addBoldTag(S,words))