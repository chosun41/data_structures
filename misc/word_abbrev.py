def validWordAbbreviation(word,abbr):
    i, j = 0, 0
    n, m = len(word), len(abbr)
    
    while i < n and j < m:
        
        if word[i] == abbr[j]: # if not while
            i += 1
            j += 1
            continue
        
        if not abbr[j].isnumeric():
            return False
        
        start = j
        while j < m and abbr[j].isnumeric():
            j += 1
            
        num = int(abbr[start:j])
        i += num
        
    return i == n and j == m

if __name__ == '__main__':

    # A string can be abbreviated by replacing any number of non-adjacent substrings with their lengths. For example, a string such as "substitution" could be abbreviated as (but not limited to):

    # "s10n" ("s ubstitutio n")
    # "sub4u4" ("sub stit u tion")
    # "12" ("substitution")
    # "su3i1u2on" ("su bst i t u ti on")
    # "substitution" (no substrings replaced)
    # "s010n" (leading zeros in numbers are allowed)
    # Note that "s55n" ("s ubsti tutio n") is not a valid abbreviation of "substitution" because the replaced substrings are adjacent.

    # Given a string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

    print(validWordAbbreviation(word = "internationalization", abbr = "i12iz4n"))

    print(validWordAbbreviation(word = "apple", abbr = "a2e"))

    print(validWordAbbreviation(word = "sabcdefghijn", abbr = "s010n"))