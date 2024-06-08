def firstRepeatedChar(A):
    size=len(A)
    count=[0]*256 #ascii
    for i in range(size):
        count[ord(A[i])]+=1
        if count[ord(A[i])]==2:
            return A[i]
        if i==size-1:
            print("no repeated characters")
    
if __name__ =='__main__':

    print(firstRepeatedChar("careermonk"))