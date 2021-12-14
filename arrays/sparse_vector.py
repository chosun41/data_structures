class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n              

    def dotProduct(self, vec):
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result

if __name__=='__main__':
    # time: O(n)
    # space: O(L) - L num of non zero items
    print()
    nums1 = [1,0,0,2,3]
    nums2 = [0,3,0,4,0]
    s1 = SparseVector(nums1)
    s2 = SparseVector(nums2)
    print(s1.dotProduct(s2))