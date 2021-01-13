from collections import defaultdict, Counter, deque

def alienOrder(words):

    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c : 0 for word in words for c in word})

    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words... create n-1 pairs out of n words
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else: # executed if break not executed, thus all letters agree
            if len(second_word) < len(first_word): 
                return ""
            
    print(adj_list)
    print(in_degree)

    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)

    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)

if __name__ == '__main__':
    
    # time: O(c) - letters of every word in words
    # space: O(1)
    
    # basically make a topological ordering out of edges between letters of dictionary order
    print(alienOrder(["wrth","wrt"]))
    print(alienOrder(["wrt","wrf","er","ett","rftt"]))
    print(alienOrder(["wrt","wrf","wrt"]))