import collections
def intersection(n1, n2):
    return list(set(n1) & set(n2))


def intersection2(nums1, nums2):
    return  list((collections.Counter(nums1)&collections.Counter(nums2)).elements())
    
if __name__ == '__main__':
    # time: O(n+m)
    # space: O(min(n,m))
    # no duplicates
    print(intersection(n1 = [1,2,2,1], n2 = [2,2]))
    # duplicates
    print(intersection2([1,2,2,1], [2,2]))