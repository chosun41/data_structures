def levenshtein_distance(word1,word2):
    memo = {}
    
    def dfs(i, j):
        if i == 0 or j == 0: return j or i
                    
        if (i,j) in memo:
            return memo[(i,j)]
        
        if word1[i-1] == word2[j-1]:
            ans = dfs(i-1, j-1)
        else: 

            ans = 1 + min(
                dfs(i, j-1),  # insert
                dfs(i-1, j),  # delete
                dfs(i-1, j-1) # replace
                )
            
        memo[(i,j)] = ans
        return memo[(i,j)]
    
    return dfs(len(word1), len(word2))

if __name__ == '__main__':
    
    # two strings A of length m and B of length n transform A into B with a minimum number of operations
    # deletion,insertion,change character
    
    # time: O(mn), space: O(mn)
    a="Helloworld"
    b="Hallowerld"
    print(levenshtein_distance(a,b))