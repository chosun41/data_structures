def wonderfulSubstrings(word):
    mask = 0
    mask_count = [0] * 1024
    mask_count[mask] += 1
    res = 0

    for letter in word:
        mask ^= 1 << ord(letter) - ord("a")
        res += mask_count[mask]
        for i in range(10):
            res += mask_count[mask ^ 1 << i]
        mask_count[mask] += 1
    return res

if __name__ == '__main__':
    
    #  A wonderful string is a string where at most one letter appears an odd number of times.

    # For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
    # Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

    # A substring is a contiguous sequence of characters in a string.

    

    # Example 1:

    # Input: word = "aba"
    # Output: 4
    # Explanation: The four wonderful substrings are underlined below:
    # - "aba" -> "a"
    # - "aba" -> "b"
    # - "aba" -> "a"
    # - "aba" -> "aba"
    # Example 2:

    # Input: word = "aabb"
    # Output: 9
    # Explanation: The nine wonderful substrings are underlined below:
    # - "aabb" -> "a"
    # - "aabb" -> "aa"
    # - "aabb" -> "aab"
    # - "aabb" -> "aabb"
    # - "aabb" -> "a"
    # - "aabb" -> "abb"
    # - "aabb" -> "b"
    # - "aabb" -> "bb"
    # - "aabb" -> "b"
    # Example 3:

    # Input: word = "he"
    # Output: 2
    # Explanation: The two wonderful substrings are underlined below:
    # - "he" -> "h"
    # - "he" -> "e"

    print(wonderfulSubstrings("aba"))
    print(wonderfulSubstrings("aabb"))

    # idea: we don't need to know exact substring to define if it's "wonderful" or not
    #   but rather if number of occurrences of each letter is odd/even;
    #   so there are only two states for each letter, so we can use binary mask to represent any substring
    #
    #   for example "0101" represents: ("d" even number, "c" - odd, "b" - even, "a" - odd);
	#   
	#  a mask will represent a prefix of word [0..k] where `0 <= k < len(word)`
	#  if we have two masks that represent prefixes [0..k] and [0..p], where `p > k`,
	#  then substring [k+1..p] is "wonderful" if:
	#     1. two masks are equal (all letters in substring [k+1..p] have even frequency)
	#     2. or two masks are 1 bit different (only one letter in substring [k+1..p] has odd frequency)
	#
	#   we can test this with XOR operator:
	#       if (mask_0_k ^ mask_0_p) == mask_with_0_or_1_bit_set => we have a "wonderful" substring
    #
    #   we can iterate through word and:
	#       1. compute a mask based on previous mask (switch bit for corresponding letter)
	#       2. find all masks that would combine with current one a "wonderful" string (equal mask or one bit different mask)
	#       3. check how many of those masks we saw earlier and add the number to result
	#       4. memorize current mask (so it can be used on further iterations)
	#
    #   example: "ccbbc" (3 letter alphabet)
	#                     binary_index:        [111, 110, 101, 100, 011, 010, 001, 000]
    #       "" -      { mask: 000, mask_count: [  0,   0,   0,   0,   0,   0,   0, 0+1], res: 0 }
    #       "c" -     { mask: 100, mask_count: [  0,   0,   0, 0+1,   0,   0,   0,   1], res: 0 + 0 (equal masks) + 1 (1 bit different masks) = 1 }
    #       "cc" -    { mask: 000, mask_count: [  0,   0,   0,   1,   0,   0,   0, 1+1], res: 1 + 1 (equal masks) + 1 (1 bit different masks) = 3 }
    #       "ccb" -   { mask: 010, mask_count: [  0,   0,   0,   1,   0, 0+1,   0,   2], res: 3 + 0 (equal masks) + 2 (1 bit different masks) = 5 }
    #       "ccbb" -  { mask: 000, mask_count: [  0,   0,   0,   1,   0,   1,   0, 2+1], res: 5 + 2 (equal masks) + 2 (1 bit different masks) = 9 }
    #       "ccbbc" - { mask: 100, mask_count: [  0,   0,   0, 1+1,   0,   1,   0,   3], res: 9 + 1 (equal masks) + 3 (1 bit different masks) = 13 }
	#
    