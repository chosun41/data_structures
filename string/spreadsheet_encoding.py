import functools

# in excel A,B,C..X,Y,Z,AA,AB.. for columns
# implement that coverts column id to corresponding integer

def ss_decode_col_id(col):

    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

if __name__=='__main__':
    
    # time: O(n)
    
    print(ss_decode_col_id('ZZ')) # 26*26 + 26 = 702
    print(ss_decode_col_id('AA')) # 1*26+1
    
    