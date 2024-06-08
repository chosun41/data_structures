from collections import deque

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    q = deque()
    items = {}
    maxLen = 0
    
    for c in s:
        if c in items:
            poppedItem = None
            while poppedItem != c:
                poppedItem = q.popleft()
                if poppedItem in items:
                    items.pop(poppedItem)
        q.append(c)
        items[c] = c
            
        maxLen = max(maxLen, len(q))
    
    return maxLen

if __name__ == '__main__':
    
    # 3. Longest Substring Without Repeating Characters
    # Medium

    # 19557

    # 891

    # Add to List

    # Share
    # Given a string s, find the length of the longest substring without repeating characters.

    

    # Example 1:

    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.
    # Example 2:

    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.
    # Example 3:

    # Input: s = "pwwkew"
    # Output: 3
    # Explanation: The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    print(lengthOfLongestSubstring(s = "abcabcbb"))

    # "abcabcbb"
    # q=[a]
    # items = {a:a}
    # maxlen = 1

    # q=[a,b]
    # items = {a:a,b:b}
    # maxlen = 2

    # q=[a,b,c]
    # items = {a:a,b:b,c:c}
    # maxlen = 3

    # q=[b,c,a]
    # items = {b:b,c:c,a:a}
    # maxlen = 3

    # q=[c,a,b]
    # items = {c:c,a:a,b:b}
    # maxlen = 3

    # q=[a,b,c]
    # items = {a:a,b:b,c:c}
    # maxlen = 3

    # q=[c,b]
    # items = {c:c,b:b}
    # maxlen = 3

    # q=[b]
    # items = {b:b}
    # maxlen = 3