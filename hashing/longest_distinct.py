def longest_subarray_with_distinct_entries(A) -> int:

    # Records the most recent occurrences of each entry.
    most_recent_occurrence = {}
    longest_dup_free_subarray_start_idx = result = 0
    
    for i, a in enumerate(A):
        # Defer updating dup_idx until we see a duplicate.
        if a in most_recent_occurrence:
            dup_idx = most_recent_occurrence[a]
            # A[i] appeared before. Did it appear in the longest current
            # subarray?
            if dup_idx >= longest_dup_free_subarray_start_idx:
                result = max(result, i - longest_dup_free_subarray_start_idx)
                longest_dup_free_subarray_start_idx = dup_idx + 1
        most_recent_occurrence[a] = i
    return max(result, len(A) - longest_dup_free_subarray_start_idx)


if __name__ == '__main__':
    
    # find longest subarray where all entries are distinct
    # ['s','f','e','t','w'] -> 5
    
    # time: 0(n)
    
    A=['f','s','f','e','t','w','e','n','w','e']
    print(longest_subarray_with_distinct_entries(A))
    
    # 0. most_recent_occurrence = {}
    #    longest_dup_free_subarray_start_idx = 0
    #    result = 0
    #    i,a=0,'f' 
    #    most_recent_occurrence = {'f':0}
    #    longest_dup_free_subarray_start_idx = 0
    #    result = 0
    # 1. most_recent_occurrence = {'f':0}
    #    longest_dup_free_subarray_start_idx = 0
    #    result = 0
    #    i,a=1,'s' 
    #    most_recent_occurrence = {'f':0,'s':1}
    #    longest_dup_free_subarray_start_idx = 0
    #    result = 0
    # 2. most_recent_occurrence = {'f':0,'s':1}
    #    longest_dup_free_subarray_start_idx = 0
    #    result = 0
    #    i,a=2,'f' 
    #    dup_idx = 0
    #    most_recent_occurrence = {'f':1,'s':1}
    #    longest_dup_free_subarray_start_idx = dup_idx + 1=1
    #    result = max(result, i - longest_dup_free_subarray_start_idx)=2
    # 3. most_recent_occurrence = {'f':1,'s':1}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    #    i,a=3,'e' 
    #    most_recent_occurrence = {'f':1,'s':1,'e':3}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    # 4. most_recent_occurrence = {'f':1,'s':1,'e':3}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    #    i,a=4,'t' 
    #    most_recent_occurrence = {'f':1,'s':1,'e':3,'t',4}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    # 5. most_recent_occurrence = {'f':1,'s':1,'e':3,'t',4}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    #    i,a=5,'w' 
    #    most_recent_occurrence = {'f':1,'s':1,'e':3,'t',4,'w':5}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    # 6. most_recent_occurrence = {'f':1,'s':1,'e':3,'t',4}
    #    longest_dup_free_subarray_start_idx = 1
    #    result = 2
    #    i,a=6,'e' 
    #    dup_idx = 3
    #    most_recent_occurrence = {'f':1,'s':1,'e':6,'t',4,'w':5}
    #    longest_dup_free_subarray_start_idx = 3 + 1= 4
    #    result = max(result, i - longest_dup_free_subarray_start_idx)=max(2,6-3)=3
    # 7. most_recent_occurrence = {'f':1,'s':1,'e':3,'t',4}
    #    longest_dup_free_subarray_start_idx = 4
    #    result = 3
    #    i,a=7,'n' 
    #    most_recent_occurrence = {'f':1,'s':1,'e':6,'t',4,'w':5,'n':7}
    #    longest_dup_free_subarray_start_idx = 4
    #    result =3
    # 8. most_recent_occurrence = {'f':1,'s':1,'e':6,'t',4,'w':5,'n':7}
    #    longest_dup_free_subarray_start_idx = 4
    #    result = 2
    #    i,a=8,'w' 
    #    dup_idx = 5
    #    most_recent_occurrence = {'f':1,'s':1,'e':6,'t',4,'w':8,'n':7}
    #    longest_dup_free_subarray_start_idx = 5 + 1= 6
    #    result = max(result, i - longest_dup_free_subarray_start_idx)=max(2,8-4)=4
    # 9. most_recent_occurrence = {'f':1,'s':1,'e':6,'t',4,'w':8,'n':7}
    #    longest_dup_free_subarray_start_idx = 4
    #    result = 2
    #    i,a=9,'e' 
    #    dup_idx = 6
    #    most_recent_occurrence = {'f':1,'s':1,'e':9,'t',4,'w':8}
    #    longest_dup_free_subarray_start_idx = 6 + 1= 7
    #    result = max(result, i - longest_dup_free_subarray_start_idx)=max(4,9-4)=5
    
    # max(result, len(A) - longest_dup_free_subarray_start_idx) = max(5,10-7)=max(5,3)=5
    