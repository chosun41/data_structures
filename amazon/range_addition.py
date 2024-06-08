def getModifiedArray(length, updates):

    ans = [0] * length
    for start, end, value in updates:
        ans[start] += value
        end += 1
        if end < len(ans):
            ans[end] -= value
        print(ans)

    for i in range(1, len(ans)):
        ans[i] += ans[i-1]

    return ans

if __name__ == '__main__':
    
    # You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

    # You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

    # Return arr after applying all the updates.

    

    # Example 1:


    # Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
    # Output: [-2,0,3,5,3]
    # Example 2:

    # Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
    # Output: [0,-4,2,2,2,4,4,-4,-4,-4]
    

    # Constraints:

    # 1 <= length <= 105
    # 0 <= updates.length <= 104
    # 0 <= startIdxi <= endIdxi < length
    # -1000 <= inci <= 1000

    # Key ideas:

    # ans is the array that will store the answer
    # Step 1: For every update with startIdx, endIdx, and incrementValue:
    # ans[startIdx] += incrementValue
    # ans[endIdx + 1] -= incrementValue (if endIdx + 1 is not out of range. If it isn't, we don't do anything)
    # Step 2: At the end, we iterate the array from index 1 (0-based indexing), and set:
    # ans[i] += ans[i-1]. This is basically prefix-sum
    # Why does this approach work? Let's go over an example. Supposed we have the input:

    # length = 5, updates = [[1,3,2]]

    # Notice how we have only 1 update to process. Let's perform Steps 1 and 2 from the key idea section above.

    # Step 1: The value of ans will be:

    # [0, 2, 0, 0, -2] (we updated index 1 and 4)

    # Step 2: The value of ans will be:

    # [0, 2, 2, 2, 0]

    # Notice how the 4-th index gets back to 0. This is because as we cascade the value index 0 to the end of the array, if we don't have:

    # ans[endIdx + 1] -= incrementValue 
    # Our array will be come
    # [0, 2, 2, 2, 2]. The bold number is of incorrect value since we only want to update from indices 1 to 3. Therefore, we need to account for the indices that we don't want to add incrementValue to when we perform step 2. How do we do that? By initially setting those indices to the opposite of incrementValue so when we perform the prefix sum step (step 2), the values at those indices will be 0.

    # Here is the complete code:

    print(getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]))
    # [-2, 0, 3, 5, 3]

    # 0,0,0,0,0
    # 0,2,0,0,-2
    # 0,2,3,0,-2
    # -2,2,3,2,-2
    # -2,0,3,5,3