def removeAdjacentDuplicates(x):
    stkptr = -1
    i = 0
    size = len(x)
    while i < size:
        if (stkptr == -1 or x[stkptr] != x[i]):
            stkptr += 1
            x[stkptr] = x[i]
            i += 1
        else:
            while i < size and x[stkptr] == x[i]:
                i += 1
            stkptr -= 1
    stkptr += 1
    x = x[0:stkptr]
    return x

if __name__=='__main__':
    
    print(removeAdjacentDuplicates(['6', '2', '4', '1', '2', '1', '2', '2', '1']))