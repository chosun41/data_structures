import collections

def lengthOfLongestSubstringKDistinct(s, k):
    left, right, dic, ans = 0, 0, collections.Counter(), 0
    while right < len(s):
        dic[s[right]] +=1
        right += 1
        while len(dic) > k:
            dic[s[left]] -= 1
            if dic[s[left]] == 0:
                del dic[s[left]]
            left += 1
        ans = max(ans, right - left)
    return ans


if __name__ == '__main__':
    # time: O(n)
    # space: O(k)
    s = "eceba"
    k = 2
    print(lengthOfLongestSubstringKDistinct(s, k))