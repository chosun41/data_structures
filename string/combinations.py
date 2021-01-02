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
    
    # elems='abc',s='',idx=0,li=[]
    # for i in range(0,3):
    # i=0, s='a', li=['a']
        # combination('abc','a',1,['a'])
        # for i in range(1,3):
        # i=1,s='ab',li=['a','ab']
            # combination('abc','ab',2,['a','ab'])
            # for i in range(2,3):
            # i=2,s='abc',li=['a','ab','abc']
                # combination('abc','abc',3,['a','ab','abc'])
                # for i in range(3,3)
            # s='ab'
        # i=2,s='ac',li=['a','ab','abc','ac']
            # combination('abc','ac',3,['a','ab','abc','ac'])
            # for i in range(3,3)
    # s='' 
    # i=1, s='b', li=['a','ab','abc','ac','b']
        # combination('abc','b',2,['a','ab','abc','ac','b'])
        # for i in range(2,3):
        # i=2,s='bc',li=['a','ab','abc','ac','b','bc']
            # combination('abc','bc','3,li)
    # s=''
    # i=2, s='c', li=['a','ab','abc','ac','b','bc','c']
        # combination('abc','c',3,li)