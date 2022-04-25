def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    def dfs(i):
        if i == len(s):
            return [""]
        res = []
        for j in range(i, len(s)):
            head = s[i:j+1] # prefix
            if head in wordDict:
                tmp = dfs(j+1) # search for next word
                for string in tmp:
                    string = head +" "+string
                    res.append(string.strip())
        return res

    return dfs(0)

if __name__=='__main__':
    
    # split spaces and make sentences using dictionary below
    # time and space: O(lw) l=len sting, w= len dictionary
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(wordBreak(s, wordDict))
    
    # i=0,j=3,head=pine,tmp=dfs(4) # pine apple pen apple, pine applepen apple
        # i=4,j=8,head=apple,tmp=dfs(9) 
            # i=9,j=11,head=pen,tmp=dfs(12) 
                #i=12,j=16,head=apple,tmp=dfs(17) 
        # i=4,j=11,head=applepen,tmp=dfs(12) 
            # i=12,j=16,head=apple,tmp=dfs(17) 
    # i=0,j=8,head=pineapple,tmp=dfs(9) # pineapple pen apple
        # i=9,j=11,head=pen,tmp=dfs(12)
            #i=12,j=16,head=apple,tmp=dfs(17)