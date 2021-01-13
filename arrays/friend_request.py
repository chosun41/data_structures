import collections
def numFriendRequests(ages):
    """
    :type ages: List[int]
    :rtype: int
    """
    group = collections.Counter(ages)
    res = 0
    for key1, val1 in group.items():
        for key2, val2 in group.items():
            if key1 > key2 and key2 > 0.5*key1+7:
                if key1 != key2:
                    res += val1 * val2
            elif key1 == key2 and key1 > 0.5*key2+7:
                res += val1 * val2 
        if key1 > 0.5*key1+7:
            res -= val1 
    return res

if __name__=='__main__':
    # time: O(a^2 + n)
    # space: O(a) - a is number of distinct ages
    # each index contains age of a person
    # person b not make friend request to person b
    # age[B] <= 0.5 * age[A] + 7
    # age[B] > age[A]
    # age[B] > 100 && age[A] < 100
    # first count ages then compare
    print(numFriendRequests([16,17,18]))
    print(numFriendRequests([20,30,100,110,120]))
        
        