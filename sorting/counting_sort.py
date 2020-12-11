def countingSort(array):
    size = len(array)
    output = [0] * size
    array_max=max(array)+1

    # Initialize count array
    count = [0] * array_max

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, array_max):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        
    return output

if __name__ == '__main__':
    
    # time: 0(n+k), space: O(max) but assumptions have to hold, assumes each integer in the range of 1 to K
    
    data = [4, 2, 2, 8, 3, 3, 1]
    print(countingSort(data))
