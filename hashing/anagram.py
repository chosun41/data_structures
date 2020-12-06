import collections

def find_anagrams(dictionary):

    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        # sorted actually splits the string into a list of characters and then you have to join them back again
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    print(sorted_string_to_anagrams)
    return [group for group in sorted_string_to_anagrams.values()]

if __name__ =='__main__':
    
    # time: O(n mlogm) - n calls to sort and n insertions into the hash table. n length of list, m string length
    
    # basically when strings are sorted, we can check if they are equivalent and group them together 
    print(find_anagrams(['debitcard','elvis','silent','badcredit','lives','freedom','listen','levis','money']))