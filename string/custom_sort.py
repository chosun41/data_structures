import collections
def customSortString(S, T):
    # count[char] will be the number of occurrences of
    # 'char' in T.
    count = collections.Counter(T)
    ans = []

    # Write all characters that occur in S, in the order of S.
    for c in S:
        ans.append(c * count[c])
        # Set count[c] = 0 to denote that we do not need
        # to write 'c' to our answer anymore.
        count[c] = 0

    # Write all remaining characters that don't occur in S.
    # That information is specified by 'count'.
    for c in count:
        ans.append(c * count[c])

    return "".join(ans)

if __name__=='__main__':
    # time: O(S+T)
    # space: O(T)
    S = "cba"
    T = "abcd"
    # sort t by s
    print(customSortString(S,T))