from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        print(self.dict)
        print(self.list)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

if __name__=='__main__':

    # Implement the RandomizedSet class:

    # RandomizedSet() Initializes the RandomizedSet object.
    # bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    # bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    # int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
    # You must implement the functions of the class such that each function works in average O(1) time complexity.

    # time: O(1)
    # space: O(N)

    randomizedSet = RandomizedSet();
    print(randomizedSet.insert(1)); # Inserts 1 to the set. Returns true as 1 was inserted successfully.
    print(randomizedSet.remove(2)); # Returns false as 2 does not exist in the set.
    print(randomizedSet.insert(2)); # Inserts 2 to the set, returns true. Set now contains [1,2].
    print(randomizedSet.getRandom()); # getRandom() should return either 1 or 2 randomly.
    print(randomizedSet.remove(1)); # Removes 1 from the set, returns true. Set now contains [2].
    print(randomizedSet.insert(2)); # 2 was already in the set, so return false.
    print(randomizedSet.getRandom()); # Since 2 is the only number in the set, getRandom() will always return 2.