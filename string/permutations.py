def recursivePermutations(elems, soFar):
    if len(elems) == 0:
        yield soFar
    else:
        for i in range(0, len(elems)):
            for perm in recursivePermutations(elems[0:i] + elems[i + 1:], soFar + [elems[i]]):
                yield perm

def permutations(elems):
    for perm in recursivePermutations(elems, []):
        print(perm)
        
if __name__=='__main__':
    elems = [1, 2, 3]
    permutations(elems)