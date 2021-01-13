
def toGoatLatin(S):
    def proc(idx, word):
        if word[0] not in 'aeiouAEIOU':
            word = word[1:] + word[0]

        return word + 'ma' + ('a' * idx)

    return ' '.join([proc(i, w) for i, w in enumerate(S.split(), 1)])
    
if __name__=='__main__':
    #     If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    # For example, the word 'apple' becomes 'applema'.

    # If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    # For example, the word "goat" becomes "oatgma".

    # Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    # For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
    print(toGoatLatin("goat"))