import collections

def minStickers(stickers,target):
    stickers, map = [collections.Counter(s) for s in stickers if set(s) & set(target)], {}
    def dfs(target):
        if not target: 
            return 0
        if target in map: 
            return map[target]
        cnt, res = collections.Counter(target), float('inf')
        for c in stickers: # traverse the stickers to get new target
            if c[target[0]] == 0: 
                continue # we can make sure the 1st letter will be removed to reduce the time complexity
            nxt = dfs(''.join([s * t for (s, t) in (cnt - c).items()]))
            if nxt != -1: 
                res = min(res, 1 + nxt)
        map[target] = -1 if res == float('inf') else res
        return map[target]
    return dfs(target)

if __name__ == '__main__':

    # We are given n different types of stickers. Each sticker has a lowercase English word on it.

    # You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

    # Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

    # Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

    print(minStickers(stickers = ["with","example","science"], target = "thehat"))

