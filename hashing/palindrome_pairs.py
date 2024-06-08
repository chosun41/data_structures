def palindromePairs(words):
    d = {}
    for i, w in enumerate(words):
        d[w[::-1]] = i
    print(d)
    indices = set()
    for i, w in enumerate(words):
        for j in range(len(w) + 1): 
            print(j)
            prefix = w[:j]
            print(prefix)
            postfix = w[j:]
            print(postfix)
            if prefix in d and i != d[prefix] and postfix == postfix[::-1]: #for in b/t letters
                indices.add((i, d[prefix]))
            if postfix in d and i != d[postfix] and prefix == prefix[::-1]: #for in b/t letters
                indices.add((d[postfix], i))
            print(indices)

    return [list(p) for p in indices]
    
if __name__ == '__main__':
    # put pairs of indexes when concatenated create palindrome
    # time: O(n*k^2) space: O(n)
    # k is length of longest word
    print(palindromePairs(["abcd","dcba","lls","s","sssll"]))