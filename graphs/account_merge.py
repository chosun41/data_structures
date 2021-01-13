import collections

class UnionFind():
    def __init__(self, accounts):
        self.uf = [0]*len(accounts)
        self.elist = [set()]*len(accounts)
        for i,a in enumerate(accounts):
            self.elist[i] = set(a[1:])
            self.uf[i] = i
    
    def find(self, i):
        while self.uf[i] != i:
            self.uf[i] = self.uf[self.uf[i]]
            i = self.uf[i]
        return i
    
    def union(self,x,y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1==p2:
            return
        if p1>p2:
            x,y=y,x
            p1,p2=p2,p1
        self.uf[p2] = p1
        self.elist[p1] = self.elist[p1].union(self.elist[p2])
        self.elist[p2] = set()


def accountsMerge(accounts):
    ufind = UnionFind(accounts)
    emails = collections.defaultdict(int)
    for i,a in enumerate(accounts):
        for e in a[1:]:
            if e not in emails:
                emails[e] = i
            else:
                ufind.union(i,emails[e])

    ans = []
    print(ufind.uf)
    print(ufind.elist)
    for i in range(len(accounts)):
        if len(ufind.elist[i]):
            ans += [accounts[i][0]] + sorted(list(ufind.elist[i])),
    return ans

if __name__ == '__main__':
    
    # time: AlogA
    # space: A
    
    accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(accountsMerge(accounts))