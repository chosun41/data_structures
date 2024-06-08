class Trie():

    def __init__(self):
        self._end = '*'
        self.trie = dict()

    def __repr__(self):
        return repr(self.trie)

    def make_trie(self, *words):
        trie = dict()
        for word in words:
            temp_dict = trie
            for letter in word:
                temp_dict = temp_dict.setdefault(letter, {})
            temp_dict[self._end] = self._end
        self.trie = trie
        return trie

    def find_word(self, word):
        sub_trie = self.trie

        for letter in word:
            if letter in sub_trie:
                sub_trie = sub_trie[letter]
            else:
                return False

        if self._end in sub_trie:
            return True
        else:
            return False

    def add_word(self, word):
        if self.find_word(word):
            print("Word Already Exists")
            return self.trie

        temp_trie = self.trie
        for letter in word:
            if letter in temp_trie:
                temp_trie = temp_trie[letter]
            else:
                temp_trie = temp_trie.setdefault(letter, {})
        temp_trie[self._end] = self._end
        return temp_trie
    
if __name__ == '__main__':
    
    # node with children for each letter of the alphabet
    # huge memory but O(L) - L is length of the word
    my_trie = Trie()
    my_trie.add_word('head')
    my_trie.add_word('hi')
    my_trie.add_word('howdy')
    print(my_trie)

    print(my_trie.find_word("hi"))
    print(my_trie.find_word("how"))
    print(my_trie.find_word("head"))