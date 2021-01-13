def minRemoveToMakeValid(s: str) -> str:
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    print(stack)
    print(indexes_to_remove)
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)
    
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