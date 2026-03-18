def fullJustify(words, maxWidth):
    result, cur, num_of_letters = [], [], 0

    for word in words:
        if num_of_letters + len(word) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            result.append(''.join(cur))
            cur, num_of_letters = [], 0

        cur += [word]
        num_of_letters += len(word)

    return result + [' '.join(cur).ljust(maxWidth)]

if __name__ == '__main__':

    print(fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
    print(fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))

    #Intuition

    # Initialize an empty result list to store the justified lines, an empty current line (cur), and a variable to keep track of the total number of letters in the current line (numOfLetters).

    # Iterate through the list of words one by one.

    # For each word:

    # Check if adding the word to the current line would exceed the maximum width. If it would, it's time to justify the current line.

    # Calculate the number of spaces that need to be added to distribute them evenly. This is done by finding the difference between the maximum width and the total number of letters in the current line.

    # Distribute these spaces evenly among the words in the current line. The modulo operator is used to ensure that spaces are distributed evenly, even if there are more words than spaces.

    # Add the justified line to the result list.

    # Clear the current line and reset the numOfLetters counter.

    # Continue adding words to the current line until you reach a point where adding the next word would exceed the maximum width.

    # For the last line of text, left-justify it by adding spaces between words. Ensure that the total width of the line matches the maximum width.

    # Return the list of justified lines as the final result.

    # Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    # You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    # Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    # For the last line of text, it should be left-justified, and no extra space is inserted between words.

    # Note:

    # A word is defined as a character sequence consisting of non-space characters only.
    # Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    # The input array words contains at least one word.
    

    # Example 1:

    # Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    # Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    # Example 2:

    # Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    # Output:
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    # Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    # Note that the second line is also left-justified because it contains only one word.
    # Example 3:

    # Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    # Output:
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
    

    # Constraints:

    # 1 <= words.length <= 300
    # 1 <= words[i].length <= 20
    # words[i] consists of only English letters and symbols.
    # 1 <= maxWidth <= 100
    # words[i].length <= maxWidth