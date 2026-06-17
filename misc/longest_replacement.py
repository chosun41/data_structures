class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_f = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_f = max(max_f, count[s[r]])
            
            # window_len - most_frequent_char_count > k? Shrink window.
            # only care about if beat previous record, not whether it is valid
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res

# --- Test Examples ---
if __name__ == "__main__":

    # You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    # Return the length of the longest substring containing the same letter you can get after performing the above operations.

    

    # Example 1:

    # Input: s = "ABAB", k = 2
    # Output: 4
    # Explanation: Replace the two 'A's with two 'B's or vice versa.
    # Example 2:

    # Input: s = "AABABBA", k = 1
    # Output: 4
    # Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    # The substring "BBBB" has the longest repeating letters, which is 4.
    # There may exists other ways to achieve this answer too.
    
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))   # Expected: 4
    print(sol.characterReplacement("AABABBA", 1))# Expected: 4