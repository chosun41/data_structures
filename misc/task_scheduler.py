def leastInterval(tasks, n):
    # frequencies of the tasks
    frequencies = [0] * 26
    for t in tasks:
        frequencies[ord(t) - ord('A')] += 1

    # max frequency
    f_max = max(frequencies)
    print(f_max)
    # count number of times max shows up
    n_max = frequencies.count(f_max) # count
    print(n_max)

    # max len tasks
    return max(len(tasks), (f_max - 1) * (n + 1) + n_max) # pattern is freq max -1 sets of n+1 windows and n max at the end
    # rationale for formula 
    # f_max - 1 - number of groups made
    # (n+1) - number of members in each group
    # n_max - leftover that didnt fit into any group

if __name__=='__main__':
    # time: O(n) number of tasks
    # space: O(1)
    # n indicates the length of time between two of the same tasks, what is the minimum amoun of time
    # if every index indicates one unit of time
    print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)) # A-B-1-A-B-1-A-B
    # fmax=3,nmax=2,len(tasks)=6, 2*3+2=8
    print(leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)) # A-B-C-A-D-1-A-E-1-A-F-1-A-G-1-A
    # fmax=6,nmax=1,len(tasks)=12, (5)*(3)+1=16