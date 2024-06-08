import string

def int_to_string(x):

    neg=False
    if x<0:
        neg=True
        x=-x

    res=[]

    while x:
        res.append(str(x%10))
        x//=10
    return ''.join(['-']+res[::-1] if neg else res[::-1])


def string_to_int(s):

    neg=False
    if s[0]=='-':
        neg=True
        s=s[1:]

    num=0

    for c in s:
        num = num*10 + (ord(c)-ord('0'))

    return -1*num if neg else num 


if __name__=='__main__':

    x=int_to_string(-321)
    print(x)
    print(type(x))
    y=string_to_int('-321')
    print(y)
    print(type(y))
    
    