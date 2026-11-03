import collections

def accountsMerge(accounts):
    res = []
    cache = collections.defaultdict(list)
    visited = set()
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            cache[email].append(i)

    # cache - dictionary of email to account index
    # visited - visited account indexes

    def dfs(idx, sub_res):
        if idx in visited:
            return
        visited.add(idx)
        for email in accounts[idx][1:]:
            sub_res.add(email)
            for records in cache[email]:
                dfs(records, sub_res)
        return

    for idx, acc in enumerate(accounts):
        tmp_res = set() # always a set
        dfs(idx, tmp_res)
        if tmp_res: # important to get rid of no emails left
            res.append([acc[0]] + sorted(list(tmp_res)))

    return res

if __name__ == '__main__':
    
    # time: AlogA
    # space: A
    # Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

    # Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

    # After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
    accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(accountsMerge(accounts))