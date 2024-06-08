from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
        self.data = None
        self.hits = 0
        
    def search(self):
        ans = []
        if self.is_end:
            ans.append((self.hits, self.data))
        for child in self.children.values():
            ans.extend(child.search())
        return ans
    
    def add_sentence(self, sentence, hit, i=0):
        if i == len(sentence):
            self.is_end = True
            self.data = sentence
            self.hits -= hit
        else:
            self.children[sentence[i]].add_sentence(sentence, hit, i + 1)
        
class AutocompleteSystem:

    def __init__(self, sentences, hits):
        self.trie = TrieNode()
        self.tmp = self.trie
        self.curr = []
        for i, sentence in enumerate(sentences):
            self.trie.add_sentence(sentence, hits[i])
          
    def input(self, c):
        if c == '#':
            self.trie.add_sentence(''.join(self.curr), 1)
            self.curr = []
            self.tmp = self.trie
            return []
        else:
            self.curr.append(c)
            if not self.tmp or c not in self.tmp.children:
                self.tmp = None
                return []
            self.tmp = self.tmp.children[c]
            return [a[1] for a in sorted(self.tmp.search())[:3]]

if __name__ == '__main__':
    
    # Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

    # You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

    # Here are the specific rules:

    # The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
    # The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
    # If less than 3 hot sentences exist, return as many as you can.
    # When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
    # Implement the AutocompleteSystem class:

    # AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
    # List<String> input(char c) This indicates that the user typed the character c.
    # Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
    # Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.
    

    # Example 1:

    # Input
    # ["AutocompleteSystem", "input", "input", "input", "input"]
    # [[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
    # Output
    # [null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]


     # AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
    # obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
    # obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
    # obj.input("a"); // return []. There are no sentences that have prefix "i a".
    # obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

    obj = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]) # 
    print(obj.input("i")) # There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
    print(obj.input(" ")) # // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
    print(obj.input("a")) # // return []. There are no sentences that have prefix "i a".
    print(obj.input("#")) # // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
