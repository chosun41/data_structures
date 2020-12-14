def levenshtein_distance(A, B):
    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            # A is empty so add all of B's characters.
            return B_idx + 1
        elif B_idx < 0:
            # B is empty so delete all of A's characters.
            return A_idx + 1

        if A[A_idx] == B[B_idx]:
            return compute_distance_between_prefixes(A_idx - 1, B_idx - 1)

        substitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
        add_last = compute_distance_between_prefixes(A_idx, B_idx - 1)
        delete_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
        return 1 + min(substitute_last, add_last, delete_last)

    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)

if __name__ == '__main__':
    
    # two strings A of length m and B of length n transform A into B with a minimum number of operations
    # deletion,insertion,change character
    
    # time: O(mn), space: O(mn)
    a="Helloworld"
    b="Hallowerld"
    print(levenshtein_distance(a,b))