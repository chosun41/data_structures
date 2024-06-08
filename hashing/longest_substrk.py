import collections

def lengthOfLongestSubstringKDistinct(s, k):
    left, right, dic, ans = 0, 0, collections.Counter(), 0
    while right < len(s): # go along and update dic, reset pointers and dic as you go along
        dic[s[right]] +=1
        if len(dic)>=k:
            print(left, right, dic, ans)
            while len(dic) > k: # shrink while length of dic is greter than k
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            right += 1
            ans = max(ans, right - left)
            print(left, right, dic, ans)
            print()
        else:
            right += 1
    return ans


if __name__ == '__main__':
    # time: O(n)
    # space: O(k)
    s = "eceba"
    k = 2
    print(lengthOfLongestSubstringKDistinct(s, k))