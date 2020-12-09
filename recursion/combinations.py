def combinations(n, k):
    
    def directed_combinations(offset, partial_combination):
        
        if len(partial_combination) == k:
            result.append(partial_combination.copy())
            return

        # Generate remaining combinations over {offset, ..., n - 1} of size
        # num_remaining.
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    result = []
    directed_combinations(1, [])
    return result


if __name__ == '__main__':
    
    # O(n (n k))
    print(combinations(5, 2))