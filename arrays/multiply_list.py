# time: O(mn) m is longer length string

def multiply(num1, num2):

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    
    # grade school algorithm in reverse
    for j in reversed(range(len(num2))):
        for i in reversed(range(len(num1))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10 # res i+j+1 not num1[i]*num2[j]
            result[i + j + 1] %= 10

    # Remove the leading zeroes.       
    result = result[next((i for i, x in enumerate(result) if x != 0), 0):] or [0]
    return [sign * result[0]] + result[1:]

def multiply2(num1,num2):
    sign = -1 if (num1[0]=='-') ^ (num2[0]=='-') else 1
    num1=num1[num1[0]=='-':]
    num2=num2[num2[0]=='-':]
    rslt=[0]*(len(num1)+len(num2))

    for j in reversed(range(len(num2))):
        for i in reversed(range(len(num1))):
            rslt[i+j+1]+=(ord(num2[i])-ord('0'))*(ord(num1[j])-ord('0'))
            rslt[i+j]+=rslt[i+j+1]//10
            rslt[i+j+1]%=10
    
    rslt=rslt[rslt[0]==0:]
    rslt[0]*=sign
    rslt=''.join(map(str,rslt))
    
    return rslt 
    
if __name__ == '__main__':
    # time: O(mn)
    # space: O(m+n)
    print(multiply([-1,2,3],[9,8,7]))
    # as strings
    print(multiply2(num1 = "-123", num2 = "987"))