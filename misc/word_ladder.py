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
                        newlayer[newWord] += [j + [newWord] for j in layer[word]] # add new word to all sequences and form new layer element newlayer not layer
        wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops, not in for loops
        layer = newlayer # move down to new layer

    return []

if __name__=='__main__':
    # change one word into the end word by only changing one letter at a time
    # space and time: O(nk) k-longest word length in wordlist
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(findLadders(beginWord, endWord, wordList))