from heapq import heappush, heappop, heapify
from collections import defaultdict
 
def HuffmanEncode(characterFrequency):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[freq, [sym, ""]] for sym, freq in characterFrequency.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == '__main__':
    
    # time: O(nlogn)
    # based on frequnecy of the words, build a tree where most frequent at top
    # need to go left append 0, need to go right append a 1
    # most frequent use fewer bytes than ones below

    inputText = "this is an example for huffman encoding"
    characterFrequency = defaultdict(int)
    for character in inputText:
        characterFrequency[character] += 1
    print(characterFrequency)
    print("\n")
    huffCodes = HuffmanEncode(characterFrequency)
    print("\n")
    print("Symbol\tFrequency\tHuffman Code")
    for p in huffCodes:
        print("%s\t%s\t%s" % (p[0], characterFrequency[p[0]], p[1]))
