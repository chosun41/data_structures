import collections

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_unordered(paragraph,keywords):

    keywords_to_cover = collections.Counter(keywords)
    result = Subarray(start=-1, end=-1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            # if the word is in keyboard decrement decrement keywords to cover and remaining to cover
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == Subarray(start=-1,end=-1) or right - left < result.end - result.start:
                result = Subarray(start=left, end=right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result

def find_smallest_subarray_ordered(paragraph,keywords):

    # Maps each keyword to its index in the keywords array.
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}

    # Since keywords are uniquely identified by their indices in keywords
    # array, we can use those indices as keys to lookup in an array.
    latest_occurrence = [-1] * len(keywords)
    # For each keyword (identified by its index in keywords array), the length
    # of the shortest subarray ending at the most recent occurrence of that
    # keyword that sequentially cover all keywords up to that keyword.
    shortest_subarray_length = [float('inf')] * len(keywords)

    shortest_distance = float('inf')
    result = Subarray(-1, -1)
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:  # First keyword.
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = (i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = (distance_to_previous_keyword + shortest_subarray_length[keyword_idx - 1])
            latest_occurrence[keyword_idx] = i

            # Last keyword, for improved subarray.
            if (keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)
    return result

if __name__ == '__main__':
    
    paragraph=['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog']

    print(find_smallest_subarray_unordered(paragraph,['cat','banana']))
    # keywords_to_cover = {banana:1,cat:1},result = Subarray(start=-1, end=-1),remaining_to_cover=2,left=0
    # right=0,p=apple,{banana:1,cat:1},remaining_to_cover=2
    # right=1,p=banana,{banana:0,cat:1},remaining_to_cover=1
    # right=2,p=apple,{banana:0,cat:1},remaining_to_cover=1
    # right=3,p=apple,{banana:0,cat:1},remaining_to_cover=1
    # right=4,p=dog,{banana:0,cat:1},remaining_to_cover=1
    # right=5,p=cat,{banana:0,cat:0},remaining_to_cover=0
    # result=Subarray(start=0,end=5),left=1
    # 5-1<5, result=Subarray(start=1,5),left=2
    # keywords_to_cover ={banana:1,cat:0},remaining_cover=1
    # right=6,p=apple,{banana:1,cat:0},remaining_to_cover=1
    # right=7,p=dog,{banana:1,cat:0},remaining_to_cover=1
    # right=8,p=banana,{banana:0,cat:0},remaining_to_cover=0
    # 8-2>4,left=3
    # 8-3>4,left=4
    # 8-4=4,left=5
    # 8-5<4,result=Subarray(start=5,8),{banana:0,cat:1},left=6
    # right=9,p=apple
    # right=10,p=cat,{banana:0,cat:0},remaining_to_cover=0
    # 10-6>8-5,left=7
    # 10-7=8-5,left=8
    # 10-8<8-5,result=Subarray(start=8,10),{banana:1,cat:0},remaining_to_cover=1,left=9
    # right=11,p=dog
    
    print(find_smallest_subarray_ordered(paragraph,['cat','banana']))
    
    # keyword_to_idx = {cat:0,banana:1}, latest_occurrence=[-1,-1],shortest_subarray_length = [float('inf'),float('inf')],
    # shortest_distance = float('inf'),result = Subarray(-1, -1)

    ['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog']
    # i=0,p=apple
    # i=1,p=banana,keyword_idx=1,latest_occurrence=[-1,1]
    # i=2,p=apple
    # i=3,p=apple
    # i=4,p=dog
    # i=5,p=cat,keyword_idx=0,shortest_subarray_length = [1,float('inf')],latest_occurrence=[5,1]
    # i=6,p=apple
    # i=7,p=dog
    # i=8,p=banana,keyword_idx=1,distance_to_previous_keyword=8-5=3,shortest_subarray_length = [1,4],latest_occurrence=[5,8]
    # shortest_distance =4, result=Subarray(8-4+1,8)
    # i=9,p=apple
    # i=10,p=cat,keyword_idx=0,shortest_subarray_length = [1,4],latest_occurrence=[10,8]
    # i=11,p=dog
    # result=Subarray(5,8)
    
    for i, p in enumerate(paragraph):
        if p in keyword_to_idx:
            keyword_idx = keyword_to_idx[p]
            if keyword_idx == 0:  # First keyword. # update start of subarray to 1
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'): # update distance to prev keyword
                distance_to_previous_keyword = (i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = (distance_to_previous_keyword + shortest_subarray_length[keyword_idx - 1])
            latest_occurrence[keyword_idx] = i

            # Last keyword, for improved subarray.
            # update shortest distance from last keyword and result
            if (keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance):
                shortest_distance = shortest_subarray_length[-1]
                result = Subarray(i - shortest_distance + 1, i)
    return result
    
    print(find_smallest_subarray_ordered(paragraph,['banana','cat']))