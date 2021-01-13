import collections

def groupStrings(strings):
    groups = collections.defaultdict(list)
    for s in strings:
        groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
    print(groups)
    return groups.values()

if __name__=='__main__':
    print(groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))