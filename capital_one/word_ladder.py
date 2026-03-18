import collections

def findLadders(beginWord, endWord, wordList):
    if endWord not in wordList:
        return []

    wordSet = set(wordList) # faster checks against dictionary
    layer = {}
    layer[beginWord] = [[beginWord]] # stores current word and all possible sequences how we got to it

    while layer:
        newlayer = collections.defaultdict(list) # returns [] on missing keys, just to simplify code
        for word in layer:
            if word == endWord: 
                return layer[word] # return all found sequences
            for i in range(len(word)): # change every possible letter and check if it's in dictionary
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord =  word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        newlayer[newWord] += [j + [newWord] for j in layer[word]] # !!! layer[word] not layer
        wordSet -= set(newlayer.keys()) # !!! remove from wordset newlayer keys not with each word
        print(newlayer,wordSet)
        layer = newlayer # move down to new layer

    return []
    

if __name__=='__main__':
    # change one word into the end word by only changing one letter at a time
    # shortest transformation sequences
    # space and time: O(nk) k-longest word length in wordlist
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(findLadders(beginWord, endWord, wordList))

    # wordset,layer=["hot","dot","dog","lot","log","cog"],{'hit: [hit]}
    # wordset,newWord,newlayer=["dot","dog","lot","log","cog"],hot, {'hit: [hit], 'hot': [hit, hot]}
    # wordset,,newlayer=["dog","lot","log","cog"],dot, {'hit: [hit], 'hot': [hit, hot], 
    # 'dot': [hit, hot, dot]}
    # wordset,newWord,newlayer=["dog","log","cog"],lot, {'hit: [hit], 'hot': [hit, hot],
    # 'dot': [hit, hot, dot], 'lot': [hit, hot, lot]}
    # wordset,newWord,newlayer=["log","cog"],dog, {'hit: [hit], 'hot': [hit, hot],
    # 'dot': [hit, hot, dot], 'lot': [hit, hot, lot], 'dog': [hit, hot, dot, dog]}
    # wordset,newWord,newlayer=["cog"],log, {'hit: [hit], 'hot': [hit, hot],
    # 'dot': [hit, hot, dot], 'lot': [hit, hot, lot], 'dog': [hit, hot, dot, dog], 'log': [hit, hot, lot, log]}
    # wordset,newWord,newlayer=[],cog, {'hit: [hit], 'hot': [hit, hot],
    # 'dot': [hit, hot, dot], 'lot': [hit, hot, lot], 'dog': [hit, hot, dot, dog], 'log': [hit, hot, lot, log],
    # 'cog': [[hit,hot,dot,dog,cog],[hit,hot,dot,log,cog]]}