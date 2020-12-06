def find_nearest_repetition(paragraph):

    word_to_latest_index = {}
    nearest_repeated_distance = float('inf')
    nearest_repeated_word=None
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            if i - latest_equal_word<nearest_repeated_distance:
                nearest_repeated_distance = i - latest_equal_word
                nearest_repeated_word=word
        word_to_latest_index[word] = i

    return nearest_repeated_word,nearest_repeated_distance

if __name__=='__main__':
    
    # time: O(n)
    # space: O(d) - d # number of distinct entries
    
    # basically a dictionary to contain latest index
    # if it repeats then compare the diff in index and replace nearest_repeated_distance if it is closer than current
    
    print(find_nearest_repetition(['all','work','and','no','play','makes','for','no','work','no','fun','and','no','results']))