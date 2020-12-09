def combinationByRecursion(elems, s, idx, li):
    for i in range(idx, len(elems)):
        s += elems[i]
        li.append(s)
        # print s, idx
        combinationByRecursion(elems, s, i + 1, li)
        s = s[0:-1]
    return li
        
if __name__=='__main__':
    res=[]
    print(combinationByRecursion('abc', '', 0, res))