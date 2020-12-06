def firstNonRepeatedChar(A):
    size=len(A)
    count=[0]*256 #ascii
    for i in range(size):
        count[ord(A[i])]+=1

    for i in range(size):
        if count[ord(A[i])]==1:
            return A[i]
        if i==size:
            print("All characters repeating")
    
if __name__ =='__main__':

    # time: O(n)
    print(firstNonRepeatedChar("careermonk"))