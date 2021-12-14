import collections

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    length = len(s) + 1
    ans = ''
    counter_t = collections.Counter(t)
    i, required, find =0, len(counter_t), 0
    counter = collections.Counter()
    
    for j in range(len(s)):
        counter[s[j]] += 1
        if s[j] in counter_t and counter[s[j]] == counter_t[s[j]]: #increement num of find to see if it matches required
            find += 1
        while i <= j and find == required: # rest is in while i<=j
            if length > j - i + 1: # trying to find shortest length here
                ans = s[i: j+1]
                length = j - i + 1
            counter[s[i]] -= 1 # decrement left pointer and counter so you can move onto next character
            if s[i] in counter_t and counter[s[i]] < counter_t[s[i]]: 
                find -= 1
            i += 1

    return ans

if __name__=='__main__':
    # time and space: O(s+t)
    # cache - counter for t, to_find - number of letters to still search for
    print(minWindow(s = "ADOBECODEBANC", t = "ABC"))