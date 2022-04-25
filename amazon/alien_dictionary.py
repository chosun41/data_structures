def isAlienSorted(words,order):

    for i in range(1,len(words)):
        same_base=True
        curr_word=words[i]
        prev_word=words[i-1]

        for j in range(min(len(prev_word),len(curr_word))):
            if curr_word[j]==prev_word[j]:
                continue
            elif order.index(curr_word[j])>order.index(prev_word[j]):
                same_base=False
                break
            else:
                return False
        if same_base:
            if len(curr_word)>=len(prev_word):
                continue
            else:
                return False
    return True
    
if __name__ == '__main__':
    
    # time: O(w) - # of elements in words
    # space: O(1)

    words=["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
    order="zkgwaverfimqxbnctdplsjyohu"
    print(isAlienSorted(words,order))