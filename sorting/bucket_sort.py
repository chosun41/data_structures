def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

if __name__ == '__main__':
    
    # time: 0(n) 
    # split into buckets where you fall into a range
    # sort inside bucket and spit back out
    
    A = [.42, .32, .33, .52, .37, .47, .51]
    print(bucketSort(A))