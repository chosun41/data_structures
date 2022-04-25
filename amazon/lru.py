from collections import OrderedDict

# most recent is last
# least recent is first

class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        print(self.capacity)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        print(self)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value # add even if above capacity
        if len(self) > self.capacity:
            self.popitem(last = False) # pop 
        print(self)

if __name__=='__main__':

    # Implement the LRUCache class:

    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    # The functions get and put must each run in O(1) average time complexity.

    # time: O(1)
    # space: O(c) c-capacity
    # basically move to end before doing get or put

    lRUCache=LRUCache(2);
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    print(lRUCache.get(1))    # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))   # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))    # return -1 (not found)
    print(lRUCache.get(3))   # return 3
    print(lRUCache.get(4))   # return 4