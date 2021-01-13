def minWindow(s, t):
    d = {}
    for c in t:
        d[c] = d.get(c,0) + 1
    print(d)

    ToFind, ind = len(t), []
    L, R, head = -len(s)-1, -1, 0

    for i, c in enumerate(s):
        if c in d:
            ind.append(i)
            d[c] -= 1
            if d[c] >=0:
                ToFind -= 1
            if ToFind == 0:
                while d[s[ind[head]]] < 0: # s[ind[head]] is the character
                    d[s[ind[head]]] += 1
                    head += 1
                if i - ind[head] < R - L:
                    L, R = ind[head], i

                d[s[ind[head]]] += 1
                ToFind += 1
                head += 1

    return s[L:R+1]

if __name__=='__main__':
    # time and space: O(s+t)
    print(minWindow(s = "ADOBECODEBANC", t = "ABC"))