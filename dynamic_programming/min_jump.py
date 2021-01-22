def minJumps(A):
    n = len(A)
    jumps = [0] * (n)
    if (n == 0 or A[0] == 0):
        return float('infinity')

    for i in range(1, n):
        jumps[i] = float('infinity')
        for j in range(0, i): # up to i
            if (i <= j + A[j] and jumps[j] != float('infinity')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break # very important
    print(jumps)
    return jumps[n - 1]

if __name__ == '__main__':
    
    # start from 0 index, you can jump up to what value is in that index to another one
    # what is the minimum number of jumps to reach the end
    # time: O(n^2)
    # space: O(n)

    A = [1, 3, 6, 1, 0, 9]
    print("Minimum number of jumps to reach end is ", minJumps(A))

