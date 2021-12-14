def minRemoveToMakeValid(s: str) -> str:
    indx_remove=set()
    stk=[]

    for i,x in enumerate(s):
        if x=='(':
            stk.append(i)
        elif x==')':
            if not stk:
                indx_remove.add(i)
            else:
                stk.pop()

    print(indx_remove,stk)
    
    indx_remove = indx_remove.union(set(stk))
    res=""
    for i,x in enumerate(s):
        if i not in indx_remove:
            res+=x
    return res
    
if __name__ == '__main__':
    
    # time: O(n) 
    # space: O(n)

    print(minRemoveToMakeValid("lee(t(c)o)de)"))
    # i=3,stack=[3]
    # i=5,stack=[3,5]
    # i=7,stack=[3]
    # i=9,stack=[]
    # i=12,indexes_to_remove=(12)
    # lee(t(c)o)de
    print(minRemoveToMakeValid("a)b(c)d"))
    # i=1,indexes_to_remove=[1]
    # i=3,stack=[3]
    # i=5,stack=[]
    # ab(c)d
    print(minRemoveToMakeValid("))(("))
    # i=0,indexes_to_remove=(0)
    # i=1,indexes_to_remove=(0,1)
    # i=2,stack=[2]
    # i=3,stack=[2,3]
    # indexes_to_remove=(0,1,2,3)
    #""